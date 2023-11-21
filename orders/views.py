from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView, ListView, TemplateView

from common.mixins import TitleMixin
from orders.forms import SearchRoutesForms
from orders.models import Route
from orders.services import check_departure_date


class IndexView(TitleMixin, TemplateView):
    template_name = 'orders/index.html'
    title = _('Main')


class AboutUsView(TitleMixin, TemplateView):
    template_name = 'orders/about.html'
    title = _('About us')


class SearchRoutesView(LoginRequiredMixin, FormView):
    template_name = 'orders/search_routes.html'
    form_class = SearchRoutesForms


class RoutesView(LoginRequiredMixin, ListView):
    template_name = 'orders/routes.html'
    model = Route

    def get_queryset(self):
        departure_date = self.request.GET.get('departure_datetime')

        if check_departure_date(departure_date):
            return Route.objects.filter(
                route=self.request.GET.get('route'),
                departure_datetime__date=departure_date
            )

        return ()
