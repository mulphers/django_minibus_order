from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView

from common import mixins
from users import forms, models


class SignInView(mixins.TitleMixin, mixins.LogoutRequiredMixin, LoginView):
    template_name = 'users/sign_in.html'
    title = _('Sign in')
    form_class = forms.SignInForm

    def get_redirect_url(self):
        return reverse_lazy('user:profile', kwargs={'pk': self.request.user.id})


class SignUpView(mixins.TitleMixin, mixins.LogoutRequiredMixin, CreateView):
    model = models.User
    form_class = forms.SignUpForm
    template_name = 'users/sign_up.html'
    title = _("Sign up")
    success_url = reverse_lazy('user:sign_in')


class ProfileView(mixins.TitleMixin, mixins.UserCheckMixin, UpdateView):
    model = models.User
    form_class = forms.ProfileUpdateForm
    template_name = 'users/profile.html'
    title = _('Profile')

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
