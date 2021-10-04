from django.contrib import admin
from django.urls import path, include

from ocdaApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),

    path('misAlumnos', views.misAlumnos, name='misAlumnos'),
    path('dashboard', views.dashboard, name='dashboard'),


    path('auth/', include('userApp.urls'))
]
