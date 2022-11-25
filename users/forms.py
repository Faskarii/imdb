from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.core.validators import EmailValidator


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField(validators=[EmailValidator])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserChangPasswordForm(PasswordChangeForm):
    class Meta:
        model = User


class UserResetPasswordForm(PasswordResetForm):
    class Meta:
        model = User
