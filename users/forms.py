from django import forms
from .models import User


class UserLogin(forms.ModelForm):
    class Meta:
        model = User
        field = ['email', 'first_name', 'last_name', 'password']
