from django.shortcuts import render
# Create your views here.

d = {'insert_me': ''}
def index(request):
    return render(request ,'app1/index.html', d)