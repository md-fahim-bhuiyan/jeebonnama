# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Example:
    path('', views.home, name='home'),
]
