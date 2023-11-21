from django import forms

from orders.models import Route


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
