from django.urls import path
from . import views

urlpatterns = [
    # Page principale affichant la liste et les formulaires (GET)
    path('', views.liste_taches, name='index'),
    # Endpoint séparé pour gérer l'ajout d'une tâche (POST)
    path('ajouter/', views.ajouter_tache, name='ajouter_tache'),
]