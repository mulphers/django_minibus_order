from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('search/', views.SearchRoutesView.as_view(), name='search'),
    path('routes/', views.RoutesView.as_view(), name='routes'),
    path('create-order/<int:route_id>', views.CreateOrderView.as_view(), name='create_order'),
    path('cancel-order/<int:pk>', views.CancelOrderView.as_view(), name='cancel_order'),
    path('orders/', views.OrdersView.as_view(), name='orders'),
]
