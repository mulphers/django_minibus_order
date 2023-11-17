from django.contrib import admin

from orders.models import Order, Route


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    fields = (
        'route',
        'driver',
        'departure_datetime',
        'number_of_seats'
    )
    search_fields = ('driver',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'route',
        'landing_site'
    )
    readonly_fields = ('user',)
