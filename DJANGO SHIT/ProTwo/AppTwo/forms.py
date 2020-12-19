from django import forms
from django.core import validators
from .models import User

class User(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'