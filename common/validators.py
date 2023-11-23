from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

error_message = _('The phone number must be entered in the format:\n1. +375XXXXXXXXX\n2. 80XXXXXXXXX')

phone_number_validator = RegexValidator(
    regex=r'^((\+375|80)\d{9,9})$',
    message=error_message
)
