from django.urls import path
from django.urls.conf import include

from userApp import views

urlpatterns = [
    path('login/', views.login, name='login'),
    
    path('logout/', views.logOUT, name='logOUT'),
]
