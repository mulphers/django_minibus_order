from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect

from orders.models import Order, Route
from orders.services import (check_departure_date, check_exist_route,
                             check_free_seats)


class CheckCreateOrderMixin(UserPassesTestMixin):
    def test_func(self):
        route_id = self.kwargs.get('route_id')
        is_exist = check_exist_route(route_id)

        if is_exist:
            route = Route.objects.get(id=route_id)
            is_correct_date = check_departure_date(
                str(route.departure_datetime.date())
            )
        else:
            return False

        if is_correct_date:
            return check_free_seats(route)

        return False

    def handle_no_permission(self):
        return HttpResponseRedirect('/order/search')


class CheckCancelOrderMixin(UserPassesTestMixin):
    def test_func(self):
        try:
            order = Order.objects.get(id=self.kwargs.get('pk'))
            return self.request.user.id == order.user.id

        except ObjectDoesNotExist:
            return False

    def handle_no_permission(self):
        return HttpResponseRedirect('/order/orders')
