from django import forms
from django.contrib.auth.models import User
from app3.models import user_info
from django.utils.translation import gettext_lazy as _

class userforms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Must include: A-Z, a-z, numbers 1-9, optional; symbols @, #, $, *")

    

    class Meta():
        model = User
        fields = ('username', 'password')
        help_texts = {
            'password': _('Must include: A-Z, a-z, numbers 1-9, optional; symbols @, #, $, *'),
        }

class profileforms(forms.ModelForm):
    class Meta():
        model = user_info
        fields = ('portfolio', 'picture')

