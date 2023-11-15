from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from users.models import User


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': _('Enter your username')
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': _('Enter password')
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputFirstName',
        'placeholder': _('Enter your name')
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputLastName',
        'placeholder': _('Enter last name')
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputUsername',
        'placeholder': _('Enter your username')
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputEmailAddress',
        'placeholder': _('Enter your email address')
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputPassword',
        'placeholder': _('Enter password')
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputConfirmPassword',
        'placeholder': _('Confirm the password')
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
