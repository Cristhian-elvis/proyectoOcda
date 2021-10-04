from django.shortcuts import render, HttpResponse

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic import CreateView

from django.contrib.auth import authenticate, login, logout

from userApp.forms import FormularioLogin
# Create your views here.

def authentication(request):
    user = authenticate(
                request=request,
                username=request.POST['username'],
                password=request.POST['password1']
            )
    return user

def login(request):

    if request.method == 'POST':
            user = authentication(request)
            #txt = request.POST['email'] + " / "+ request.POST['password']
            #return HttpResponse("login: "+txt)
            if user is not None:
                login(request, user)
                #return HttpResponse("Logueado")
                return HttpResponseRedirect(reverse('Home'))
    else:
        form = FormularioLogin()

    return render(request, 'userApp/login.html', {'form': form})


def logOUT(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

