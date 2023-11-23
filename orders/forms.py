from django import forms

from orders.models import Order, Route


class SearchRoutesForms(forms.ModelForm):
    class DateInput(forms.DateInput):
        input_type = 'date'

    route = forms.CharField(widget=forms.Select(
        choices=Route.FromWhereToWhere.choices
    ))

    departure_datetime = forms.DateField(widget=DateInput())

    class Meta:
        model = Route
        fields = ('route', 'departure_datetime')


class CreateOrderForm(forms.ModelForm):
    landing_site = forms.CharField(widget=forms.Select(
        choices=Order.LandingSites.choices
    ))

    class Meta:
        model = Order
        fields = ('landing_site',)
