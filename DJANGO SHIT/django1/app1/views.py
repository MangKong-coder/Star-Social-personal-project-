from django.shortcuts import render
from app1.models import AccessRecord, User, Webpage,UserInfo
from . import forms
# Create your views here.

def home(request):
    return render(request, 'home.html', {'Home': ''})

webpages_list = AccessRecord.objects.order_by('date')
d = {'accrecord': webpages_list}
def index(request):
    return render(request ,'app1/index.html', d)

def form(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            s = form.save()
            print('VALIDATION SUCCESS')



    return render(request, 'form_page.html', {'forms': form})