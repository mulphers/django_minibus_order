from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class LogoutRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect(reverse_lazy('user:profile', kwargs={'pk': self.request.user.id}))


class UserCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.id == self.kwargs.get('pk')

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('user:profile', kwargs={'pk': self.request.user.id}))

        return redirect(settings.LOGIN_URL)
