from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserChangeForm
from django import forms
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")

    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "email",)


class MyPasswordChangeFrom(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(
        attrs={'autofocus': 'True',
               'autocomplete': 'current-password',
               'class': 'form-control'
               }))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password',
               'class': 'form-control',
               }))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password',
               'class': 'form-control',
               }))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password',
               'class': 'form-control',
               }))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password',
               'class': 'form-control',
               }))


class ProfileForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
        ]