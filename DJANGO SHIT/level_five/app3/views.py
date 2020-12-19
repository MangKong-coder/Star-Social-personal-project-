from django.shortcuts import render
from app3.forms import userforms, profileforms
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html', {'home':''})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('localhost:8000')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = userforms(data=request.POST)
        profile_form = profileforms(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
        
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = userforms
        profile_form = profileforms

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username, password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('localhost:8000')
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('Someone tried to login and failed')
            print(f'Username {username}, Password {password}')
            return HttpResponse('invalid inputs')
    else:
        return render(request, 'log-in.html', {})
        


