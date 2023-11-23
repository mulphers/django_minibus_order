import re
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist

from orders.models import Order, Route


def add_parameters_form(self, instance):
    route_id = self.kwargs.get('route_id')

    instance.route_id = route_id
    instance.user_id = self.request.user.id

    instance.save()


def check_departure_date(departure_date_str):
    if not re.fullmatch(r'\d{4}(-\d{2}){2}', str(departure_date_str)):
        return False

    departure_date_date = datetime.strptime(departure_date_str, '%Y-%m-%d').date()

    return departure_date_date >= datetime.today().date()


def check_exist_route(route_id):
    try:
        _ = Route.objects.get(id=route_id)
    except ObjectDoesNotExist:
        return False

    return True


def check_free_seats(route):
    return route.number_of_seats - 1 >= 0


def reduce_number_of_seats(route_id):
    route = Route.objects.get(id=route_id)
    route.number_of_seats -= 1
    route.save()


def increase_number_of_seats(order_id):
    order = Order.objects.get(id=order_id)
    route = order.route
    route.number_of_seats += 1
    route.save()
