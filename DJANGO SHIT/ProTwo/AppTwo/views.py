from django.shortcuts import render
from django.http import HttpResponse

d = {'Help_Page': ''}
def index(requests):
    return render(requests, 'AppTwo/help.html', d)
# Create your views here.
