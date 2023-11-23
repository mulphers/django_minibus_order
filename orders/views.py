from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (CreateView, DeleteView, FormView, ListView,
                                  TemplateView)

from common.mixins import TitleMixin
from orders.forms import CreateOrderForm, SearchRoutesForms
from orders.mixins import CheckCancelOrderMixin, CheckCreateOrderMixin
from orders.models import Order, Route
from orders.services import (add_parameters_form, check_departure_date,
                             increase_number_of_seats, reduce_number_of_seats)


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


class CreateOrderView(CheckCreateOrderMixin, CreateView):
    template_name = 'orders/create_order.html'
    model = Order
    form_class = CreateOrderForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        add_parameters_form(self, instance)
        reduce_number_of_seats(self.kwargs.get('route_id'))

        return HttpResponseRedirect('/order/orders')


class CancelOrderView(CheckCancelOrderMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('order:orders')

    def get(self, request, *args, **kwargs):
        increase_number_of_seats(kwargs.get('pk'))
        return self.post(request, *args, **kwargs)


class OrdersView(LoginRequiredMixin, ListView):
    template_name = 'users/orders.html'
    model = Order

    def get_queryset(self):
        return sorted(
            Order.objects.filter(user_id=self.request.user.id),
            key=lambda obj: obj.route.departure_datetime,
            reverse=True
        )
