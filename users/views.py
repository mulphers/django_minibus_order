from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from common.mixins import TitleMixin
from users import forms, models


class SignInView(TitleMixin, LoginView):
    template_name = 'users/sign_in.html'
    title = _('Sign in')
    form_class = forms.SignInForm

    def get_redirect_url(self):
        pass


class SignUpView(TitleMixin, CreateView):
    model = models.User
    form_class = forms.SignUpForm
    template_name = 'users/sign_up.html'
    title = _("Sign up")
    success_url = reverse_lazy('user:sign_in')
