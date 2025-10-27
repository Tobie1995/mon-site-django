from django.urls import path
from . import views

urlpatterns = [
    path('', views.bonjour, name='bonjour'),
]
