from django.contrib.auth.views import LogoutView
from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('sign-in/', views.SignInView.as_view(), name='sign_in'),
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
    path('sign-out/', LogoutView.as_view(), name='sign_out'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile')
]
