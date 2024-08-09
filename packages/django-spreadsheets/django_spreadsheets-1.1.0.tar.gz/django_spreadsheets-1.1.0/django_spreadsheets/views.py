# Standard Library
import operator
import os

# Django
from django.apps import apps
from django.conf import settings
from django.contrib import admin, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.encoding import escape_uri_path
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import FormView
from django.views.generic.list import BaseListView

# Third party
from formtools.wizard.views import SessionWizardView

# Local application / specific library imports
from .conf import settings as local_settings
from .exceptions import ImportValueNotFoundException
from .exporter import Exporter
from .forms import ConfigChoiceForm, FileForm, MatchForm
from .importer import Importer
from .registry import registry
from .shortcuts import include_admin_fields_for_user


class ConfigParamMixin:
    config_name = None

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.config_name = self.request.GET.get("config")
        self.config_class = registry.get_class(self.config_name)


class AdminSiteMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        app_label = "django_spreadsheets"
        context["app_label"] = app_label
        context["app_config"] = apps.get_app_config(app_label)
        context["title"] = _("Import/Export")

        context.update(admin.site.each_context(self.request))
        return context


class ImportIndex(LoginRequiredMixin, AdminSiteMixin, FormView):
    form_class = ConfigChoiceForm
    template_name = "spreadsheets/import_index.html"

    def form_valid(self, form):
        object = form.cleaned_data.get("object")
        if object is not None:
            url = reverse("spreadsheets:import-single-object", args=[object.id])
        else:
            url = reverse("spreadsheets:import-all-objects")

        config_name = form.cleaned_data.get("config")
        if config_name is not None:
            params = f"?config={config_name}"
        else:
            params = ""

        return HttpResponseRedirect(url + params)


class ExportIndex(LoginRequiredMixin, AdminSiteMixin, FormView):
    form_class = ConfigChoiceForm
    template_name = "spreadsheets/export_index.html"

    def form_valid(self, form):
        object = form.cleaned_data.get("object")
        if object is not None:
            url = reverse("spreadsheets:export-single-object", args=[object.id])
        else:
            url = reverse("spreadsheets:export-all-objects")

        config_name = form.cleaned_data.get("config")
        if config_name is not None:
            params = f"?config={config_name}"
        else:
            params = ""

        return HttpResponseRedirect(url + params)


class BaseImportModelWizardView(
    ConfigParamMixin, LoginRequiredMixin, AdminSiteMixin, SessionWizardView
):
    template_name = "spreadsheets/wizard.html"
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, "spreadsheets_import")
    )
    form_list = (
        ("file", FileForm),
        ("match", MatchForm),
    )

    def process_step(self, form):
        """
        Store the match errors in session in order to reuse them on next wizard steps
        """
        if self.config_class is None:
            return HttpResponse(f'No config found with name: "{self.config_name}"')

        if hasattr(form, "match_errors") and form.match_errors is not None:
            self.storage.data["match_errors"] = form.match_errors

        return super().process_step(form)

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)

        context["config_name"] = self.config_name

        if hasattr(form, "import_errors") and form.import_errors is not None:
            form.import_errors.sort(key=operator.attrgetter("title"))
            form.import_errors.sort(key=operator.attrgetter("order"))
            form.import_errors.sort(key=operator.attrgetter("sheet_name"))

        return context

    def get_form_kwargs(self, step=None):
        if step == "file":
            include_admin_fields = include_admin_fields_for_user(self.request.user)
            return {
                "config": self.config_class(),
                "include_admin_fields": include_admin_fields,
            }

        match_errors = self.storage.data.get("match_errors")
        if step == "match" and match_errors is not None:
            return {"match_errors": match_errors}
        return {}

    def done(self, form_list, **kwargs):
        file_form = form_list[0]
        match_form = form_list[1]

        include_admin_fields = include_admin_fields_for_user(self.request.user)
        importer = Importer(
            config=self.config_class(),
            file=file_form.cleaned_data["file"].file,
            include_admin_fields=include_admin_fields,
        )

        # Assign form to importer, so the cleaned data values can be used in it to override the file values and then update the database
        importer.match_form = match_form

        try:
            self.config_class().update_database(importer.values)
        except ImportValueNotFoundException as e:
            messages.error(self.request, str(e))
            self.storage.current_step = self.steps.first
            return self.render(self.get_form())

        for sheet_name, sheet_values in importer.values.items():
            messages.success(
                self.request,
                _("{count} items has been imported from sheet {sheet_name}.").format(
                    count=len(sheet_values), sheet_name=sheet_name
                ),
            )

        return redirect("spreadsheets:done")


class ImportSingleModelWizardView(BaseImportModelWizardView, BaseDetailView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        return super().post(*args, **kwargs)

    def get_context_data(self, form, **kwargs):
        return super().get_context_data(form=form, object=self.object, **kwargs)


class ImportAllModelsWizardView(BaseImportModelWizardView):
    ...


class BaseExportModelView(ConfigParamMixin, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        include_admin_fields = include_admin_fields_for_user(request.user)

        if self.config_class is None:
            return HttpResponse(f'No config found with name: "{self.config_name}"')

        exporter = Exporter(
            config=self.config_class(),
            include_admin_fields=include_admin_fields,
        )
        response = HttpResponse(
            content=exporter.save_to_stream(),
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml",
        )
        response[
            "Content-Disposition"
        ] = f"attachment; filename={escape_uri_path(exporter.get_file_name())}"

        return response


class ExportSingleModelView(BaseExportModelView, BaseDetailView):
    def get_queryset(self):
        queryset = super().get_queryset()

        # try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # If none of those are defined, it's an error.
        if pk is None is slug:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )

        return queryset


class ExportAllModelsView(BaseExportModelView, BaseListView):
    ...


class DoneView(LoginRequiredMixin, AdminSiteMixin, TemplateView):
    template_name = "spreadsheets/done.html"


class DownloadImportTemplateFile(BaseExportModelView, BaseListView):
    def get(self, request, *args, **kwargs):
        include_admin_fields = include_admin_fields_for_user(request.user)

        config = self.config_class()

        if self.config_class is None:
            return HttpResponse(
                _('No config found with name: "{config_name}"').format(
                    config_name=self.config_name
                )
            )

        exporter = Exporter(
            config=config,
            no_data=True,
            include_admin_fields=include_admin_fields,
        )
        response = HttpResponse(
            content=exporter.save_to_stream(),
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml",
        )
        response[
            "Content-Disposition"
        ] = f"attachment; filename={local_settings.TEMPLATE_FILE_NAME.format(config_name=str(config))}"
        return response
