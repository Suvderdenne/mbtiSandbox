from django.contrib import admin
from django.urls import path
from whois_app.views import  home

urlpatterns = [
    path('', home, name='home')
]
