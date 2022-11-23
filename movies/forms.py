from platform import release
from django import forms
from django import forms
from django.core.exceptions import ValidationError
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'release_date', 'avatar')

