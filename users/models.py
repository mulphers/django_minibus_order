from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import Base
from common.validators import phone_number_validator


class Employee(Base):
    class EmployeePosition(models.TextChoices):
        operator = 'OP', _('Operator')
        driver = 'DR', _('Driver')

    full_name = models.CharField(max_length=128)
    phone_number = models.CharField(validators=[phone_number_validator], max_length=13)
    job_title = models.CharField(max_length=2, choices=EmployeePosition.choices)

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def __str__(self):
        return f'{self.full_name} | {self.phone_number} | {self.job_title}'


class User(AbstractUser, Base):
    first_name = models.CharField(_('first name'), max_length=32)
    last_name = models.CharField(_('last name'), max_length=32)
    image = models.ImageField(upload_to='user_images', blank=True, null=True)
    phone_number = models.CharField(validators=[phone_number_validator], max_length=13)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.phone_number}'
