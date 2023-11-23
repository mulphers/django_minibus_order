from django import forms
from django.contrib.auth import forms as f
from django.utils.translation import gettext_lazy as _

from common.validators import phone_number_validator
from users.models import User


class SignInForm(f.AuthenticationForm):
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


class SignUpForm(f.UserCreationForm):
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

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputPhoneNumber',
        'placeholder': _('Enter your phone number')
    }), validators=(phone_number_validator,))

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
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2')


class ProfileUpdateForm(f.UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputFirstName'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputLastName'
    }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputPhoneNumber'
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-label',
        'id': 'userAvatar',
        'size': '50'
    }), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'image')
