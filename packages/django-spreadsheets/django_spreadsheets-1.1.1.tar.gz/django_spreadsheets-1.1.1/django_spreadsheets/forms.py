# Django
from django import forms
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

# Local application / specific library imports
from .importer import Importer
from .registry import registry


class ConfigChoiceForm(forms.Form):
    config = forms.ChoiceField(
        required=False, label=_("Choose a configuration"), choices=[]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["config"].choices = (
            (key, config) for key, config in registry.get_all_classes().items()
        )


class FileForm(forms.Form):
    match_errors = None
    import_errors = None
    import_warnings = None

    file = forms.FileField(label=_("File to import"), required=True)

    def __init__(self, config, include_admin_fields, **kwargs):
        super().__init__(**kwargs)
        self.config = config
        self.include_admin_fields = include_admin_fields
        url = reverse("spreadsheets:import-template")
        self.fields["file"].help_text = mark_safe(
            _(
                'Your file must be formatted as in the template version {config_version}: <a href="{url}?config={config_name}">Download import file template version {config_version}</a>.'
            ).format(
                config_version=self.config.version,
                url=url,
                config_name=self.config.__class__.__name__,
            )
        )

    def clean(self):
        super().clean()

        files = self.files
        if not isinstance(files, dict):
            # Sometime self.files is a MultiValueDict and sometimes a dict
            # so we always convert it to a dict
            files = dict(files)

        if not files:
            raise forms.ValidationError(_("No file were provided."))

        file_object = next(iter(files.values()))  # Get the first value of the dict
        importer = Importer(
            config=self.config,
            file=file_object.file,
            include_admin_fields=self.include_admin_fields,
        )
        # Validate the file structure and data. If there are errors, they will be stored in and display to the user
        importer.validate()
        self.match_errors = importer.match_errors
        self.import_errors = importer.import_errors
        self.import_warnings = importer.import_warnings
        self.is_full_clean = importer.is_full_clean

        if self.import_errors:
            raise forms.ValidationError(
                _(
                    "There are errors in the file. Please correct them and try importing the file again."
                )
            )


class MatchForm(forms.Form):
    """
    A MatchForm creates dynamically new fields based on the passed match errors.
    """

    def __init__(self, *args, match_errors, **kwargs):
        super().__init__(*args, **kwargs)
        self.match_errors = match_errors

        for key, match_error in self.match_errors.items():
            self.fields[key] = forms.ChoiceField(
                label=match_error["label"],
                choices=match_error["choices"],
                required=True,
            )
