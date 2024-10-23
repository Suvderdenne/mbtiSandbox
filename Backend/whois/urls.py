from django.urls import path, include
from whois_app.views import home
from whois_app.viewscvreg import cvreg

urlpatterns = [
    path('', home, name='home'),
    path('cvreg/', cvreg, name='cvreg'),
]
