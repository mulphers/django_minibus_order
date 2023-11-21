from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('search/', views.SearchRoutesView.as_view(), name='search'),
    path('routes/', views.RoutesView.as_view(), name='routes')
]
