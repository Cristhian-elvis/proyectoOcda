from django.shortcuts import render

# Create your views here.
#from .forms import formPost
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User

from ocdaApp.models import Curso#, Docente

def home(request):

    return render(
        request,
        'ocdaApp/home.html'
    )

def misAlumnos(request):
    #docentes = Docente.objects.all()

    cursos = Curso.objects.all()

    return render(
        request,
        'ocdaApp/misAlumnos.html',
        {'cursos': cursos}
    )

def dashboard(request):

    return render(
        request,
        'ocdaApp/dashboard.html'
    )
