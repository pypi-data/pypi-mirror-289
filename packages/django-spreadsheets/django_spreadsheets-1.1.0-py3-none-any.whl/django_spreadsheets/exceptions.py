# Django
from django.utils.translation import gettext_lazy as _


class ImportValueNotFoundException(Exception):
    """Raised when a value is invalid for a cell."""

    def __init__(self, model_name, field_name, value):
        super().__init__(
            _(f'`{model_name}.{field_name}` received an unknown value: "{value}".')
        )
        self.model_name = model_name
        self.field_name = field_name
        self.value = value
