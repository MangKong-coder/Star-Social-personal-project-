from django.shortcuts import render
from AppTwo.models import User
from . import forms
# Create your views here.

def home(request):
    h = {'Home_Page': ''}
    return render(request, 'home.html', h)

def user(request):
    form = forms.User()

    if request.method == 'POST':
        form = forms.User(request.POST)

        if form.is_valid():
            p = form.save()
            print('VALIDATION SUCCESS')
    return render(request, 'user.html', {'forms':form})