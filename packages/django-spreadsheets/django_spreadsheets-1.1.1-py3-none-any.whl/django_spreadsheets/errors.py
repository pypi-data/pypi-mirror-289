# Django
from django.utils.translation import gettext as _

# Third party
from openpyxl.utils.cell import get_column_letter


class ImporterError:
    order = 0


class ImporterWarning:
    order = 0


class ImporterSheetMixin:
    def __init__(self, sheet_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sheet_name = sheet_name

    def __str__(self):
        return _('Sheet "{sheet_name}"').format(sheet_name=self.sheet_name)


class ImporterCellMixin(ImporterSheetMixin):
    def __init__(self, column, row, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.column = column
        self.row = row
        self.order = column

    def __str__(self):
        message = super().__str__()
        return _("{message}, cell {column_letter}{row}").format(
            message=message, column_letter=get_column_letter(self.column), row=self.row
        )


class ImporterSheetMissing(ImporterSheetMixin, ImporterError):
    @property
    def title(self):
        return _('The sheet "{sheet_name}" is missing').format(
            sheet_name=self.sheet_name
        )

    def __str__(self):
        return _(
            'The sheet "{sheet_name}" is missing from the file you supplied. Check that the sheet has not been deleted or renamed.'
        ).format(sheet_name=self.sheet_name)


class ImporterSheetIgnored(ImporterSheetMixin, ImporterError):
    def __init__(self, sheet_name, config_sheets_names, *args, **kwargs):
        super().__init__(sheet_name, *args, **kwargs)
        self.config_sheets_names = config_sheets_names

    @property
    def title(self):
        return _('The sheet "{sheet_name}" will be ignored when importing').format(
            sheet_name=self.sheet_name
        )

    def __str__(self):
        return _(
            'The sheet "{sheet_name}" in the file you have supplied does not correspond to a sheet in the template ({sheets_names}). It will be ignored.'
        ).format(
            sheet_name=self.sheet_name, sheets_names=", ".join(self.config_sheets_names)
        )


class ImporterColumnHeaderError(ImporterCellMixin, ImporterError):
    def __init__(self, column_header, expected_column_header, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.column_header = column_header
        self.expected_column_header = expected_column_header
        self.order = -1

    @property
    def title(self):
        return _("The column name does not match the model")

    def __str__(self):
        message = super().__str__()
        return _(
            '{message} : the column name is "{column_header}" when it should be "{expected_column_header}"'
        ).format(
            message=message,
            column_header=self.column_header,
            expected_column_header=self.expected_column_header,
        )


class ImporterTypeError(ImporterCellMixin, ImporterError):
    def __init__(self, column_header, expected_type, error_message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.column_header = column_header
        self.error_message = error_message
        self.expected_type = expected_type

    def __str__(self):
        message = super().__str__()
        return _(
            '{message}, column "{column_header}", type is invalid. {error_message}'
        ).format(
            message=message,
            column_header=self.column_header,
            error_message=self.error_message,
        )

    @property
    def title(self):
        return _(
            'Column "{column_header}" must be of the type: {expected_type}'
        ).format(column_header=self.column_header, expected_type=self.expected_type)


class ImporterRequiredDataError(ImporterCellMixin, ImporterError):
    def __init__(self, column_header, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.column_header = column_header

    def __str__(self):
        message = super().__str__()
        return _("{message} : cell must no be empty").format(message=message)

    @property
    def title(self):
        return _('Column "{column_header}" is required').format(
            column_header=self.column_header
        )


class ImporterRequiredUnlessDataError(ImporterRequiredDataError):
    def __init__(self, unless_column_header, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unless_column_header = unless_column_header

    def __str__(self):
        message = super(
            ImporterRequiredDataError, self
        ).__str__()  # Skip message from direct parent
        return _(
            '{message} at least one of the columns "{column_header}" or "{unless_column_header}" must be completed'
        ).format(
            message=message,
            column_header=self.column_header,
            unless_column_header=self.unless_column_header,
        )

    @property
    def title(self):
        return _(
            'At least one of the columns "{column_header}" or "{unless_column_header}" must be completed'
        ).format(
            column_header=self.column_header,
            unless_column_header=self.unless_column_header,
        )


class ImporterRequiredIfDataError(ImporterRequiredDataError):
    def __init__(self, required_if_column_header, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.required_if_column_header = required_if_column_header

    def __str__(self):
        message = super(
            ImporterRequiredDataError, self
        ).__str__()  # Skip message from direct parent
        return _(
            '{message} column "{column_header}" must be completed if column "{required_if_column_header}" is completed'
        ).format(
            message=message,
            column_header=self.column_header,
            required_if_column_header=self.required_if_column_header,
        )

    @property
    def title(self):
        return _(
            'Columns "{column_header}" and "{required_if_column_header}" must be completed'
        ).format(
            column_header=self.column_header,
            required_if_column_header=self.required_if_column_header,
        )


class ImporterUniquenessError(ImporterSheetMixin, ImporterError):
    def __init__(self, line_number, is_duplicate_of, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.line_number = line_number
        self.is_duplicate_of = is_duplicate_of

    def __str__(self):
        return _("Line {line_number} is a duplicate of line {is_duplicate_of}").format(
            line_number=self.line_number, is_duplicate_of=self.is_duplicate_of
        )

    @property
    def title(self):
        return _("Duplicated lines")


class ImporterObjectRemovalWarning(ImporterSheetMixin, ImporterWarning):
    def __init__(self, composition, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = object

    @property
    def title(self):
        return _('The object "{object}" will be deleted during import').format(
            object=self.object
        )

    def __str__(self):
        return _(
            'The object "{object}" will be deleted during import because it does not exist in the imported file.'
        ).format(object=self.object)


class ConfigVersionWarning(ImporterWarning):
    def __init__(self, expected, found, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.expected = expected
        self.found = found if found is not None else _("unknown")

    @property
    def title(self):
        return _("The configuration version of the file is incorrect")

    def __str__(self):
        return _(
            "The configuration version of the file ({found}) is different from that expected ({expected})"
        ).format(found=self.found, expected=self.expected)
