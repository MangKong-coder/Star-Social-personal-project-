from django.shortcuts import render

# Create your views here.

con_dict = {'ind': 'Ohayo', 'number': 70}

def index(request):
    return render(request, 'index.html')

def other(request):
    return render(request, 'other.html')

def relative(request):
    return render(request, 'relative.html', con_dict)
