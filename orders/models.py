from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import Base
from users import models as users_models


class Route(Base):
    class FromWhereToWhere(models.TextChoices):
        route_1 = 'RE1', _('For example A')
        route_2 = 'RE2', _('For example B')

    route = models.CharField(max_length=3, choices=FromWhereToWhere.choices, default=FromWhereToWhere.route_1)
    departure_datetime = models.DateTimeField()
    driver = models.ForeignKey(to=users_models.Employee, on_delete=models.SET_NULL, blank=True, null=True)
    number_of_seats = models.PositiveIntegerField(default=15)

    class Meta:
        verbose_name = _('Route')
        verbose_name_plural = _('Routes')

    def __str__(self):
        return f'{self.driver} | {self.departure_datetime:%d-%m-%Y %H:%M}'


class Order(Base):
    class LandingSites(models.TextChoices):
        place_1 = 'FE1', _('For example 1')
        place_2 = 'FE2', _('For example 2')
        place_3 = 'FE3', _('For example 3')

    user = models.ForeignKey(to=users_models.User, on_delete=models.CASCADE)
    route = models.ForeignKey(to=Route, on_delete=models.CASCADE)
    landing_site = models.CharField(max_length=3, choices=LandingSites.choices)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f'{_("Route")}: {self.route.departure_datetime:%d-%m-%Y %H:%M} |' \
               f' {_("User")}: {self.user.first_name} {self.user.last_name}'
