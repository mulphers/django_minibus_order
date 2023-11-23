from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView

from common.mixins import TitleMixin
from users.forms import ProfileUpdateForm, SignInForm, SignUpForm
from users.mixins import LogoutRequiredMixin, UserCheckMixin
from users.models import User


class SignInView(
    TitleMixin,
    LogoutRequiredMixin,
    LoginView
):
    template_name = 'users/sign_in.html'
    title = _('Sign in')
    form_class = SignInForm

    def get_redirect_url(self):
        return reverse_lazy('user:profile', kwargs={'pk': self.request.user.id})


class SignUpView(
    TitleMixin,
    LogoutRequiredMixin,
    CreateView
):
    template_name = 'users/sign_up.html'
    title = _("Sign up")
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('user:sign_in')


class ProfileView(
    TitleMixin,
    UserCheckMixin,
    UpdateView
):
    template_name = 'users/profile.html'
    title = _('Profile')
    model = User
    form_class = ProfileUpdateForm

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
