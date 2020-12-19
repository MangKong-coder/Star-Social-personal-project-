from django import forms
from django.core import validators
from app1.models import UserInfo


class FormName(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'
   