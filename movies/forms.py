from platform import release
from django import forms
from django import forms

class MovieForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    release_date = forms.DateField()
    avatar = forms.ImageField(required=False)