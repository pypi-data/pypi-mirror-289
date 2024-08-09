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
        return _(f'Sheet "{self.sheet_name}"')


class ImporterCellMixin(ImporterSheetMixin):
    def __init__(self, column, row, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.column = column
        self.row = row
        self.order = column

    def __str__(self):
        message = super().__str__()
        return _(f"{message}, cell {get_column_letter(self.column)}{self.row}")


class ImporterSheetMissing(ImporterSheetMixin, ImporterError):
    @property
    def title(self):
        return _(f'The sheet "{self.sheet_name}" is missing')

    def __str__(self):
        return _(
            f'The sheet "{self.sheet_name}" is missing from the file you supplied. Check that the sheet has not been deleted or renamed.'
        )


class ImporterSheetIgnored(ImporterSheetMixin, ImporterError):
    def __init__(self, sheet_name, config_sheets_names, *args, **kwargs):
        super().__init__(sheet_name, *args, **kwargs)
        self.config_sheets_names = config_sheets_names

    @property
    def title(self):
        return _(f'The sheet "{self.sheet_name}" will be ignored when importing')

    def __str__(self):
        return _(
            f'The sheet "{self.sheet_name}" in the file you have supplied does not correspond to a sheet in the template ({", ".join(self.config_sheets_names)}). It will be ignored.'
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
            f'{message} : the column name is "{self.column_header}" when it should be "{self.expected_column_header}"'
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
            f'{message}, column "{self.column_header}", type is invalid. {self.error_message}'
        )

    @property
    def title(self):
        return _(
            f'Column "{self.column_header}" must be of the type: {self.expected_type}'
        )


class ImporterRequiredDataError(ImporterCellMixin, ImporterError):
    def __init__(self, column_header, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.column_header = column_header

    def __str__(self):
        message = super().__str__()
        return _(f"{message} : cell must no be empty")

    @property
    def title(self):
        return _(f'Column "{self.column_header}" is required')


class ImporterRequiredUnlessDataError(ImporterRequiredDataError):
    def __init__(self, unless_column_header, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unless_column_header = unless_column_header

    def __str__(self):
        message = super(
            ImporterRequiredDataError, self
        ).__str__()  # Skip message from direct parent
        return _(
            f'{message} at least one of the columns "{self.column_header}" or "{self.unless_column_header}" must be completed'
        )

    @property
    def title(self):
        return _(
            f'At least one of the columns "{self.column_header}" or "{self.unless_column_header}" must be completed'
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
            f'{message} column "{self.column_header}" must be completed if column "{self.required_if_column_header}" is completed'
        )

    @property
    def title(self):
        return _(
            f'Columns "{self.column_header}" and "{self.required_if_column_header}" must be completed'
        )


class ImporterUniquenessError(ImporterSheetMixin, ImporterError):
    def __init__(self, line_number, is_duplicate_of, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.line_number = line_number
        self.is_duplicate_of = is_duplicate_of

    def __str__(self):
        return _(
            f"Line {self.line_number} is a duplicate of line {self.is_duplicate_of}"
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
        return _(f'The object "{self.object}" will be deleted during import')

    def __str__(self):
        return _(
            f'The object "{self.object}" will be deleted during import because it does not exist in the imported file.'
        )


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
            f"The configuration version of the file ({self.found}) is different from that expected ({self.expected})"
        )
