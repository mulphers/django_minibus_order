from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(
    regex=r'^((\+375|80)\d{9,9})$',
    message='Номер телефона должен быть введен в формате:\n'
            '1. +375XXXXXXXXX\n'
            '2. 80XXXXXXXXX'
)
