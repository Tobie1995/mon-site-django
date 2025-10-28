from django.shortcuts import render, redirect
from .forms import TacheForm
from .models import Tache  # Importer le modèle Tache


def liste_taches(request):
	"""Affiche la liste des tâches et les formulaires (GET uniquement).

	- Méthode GET : affiche la liste, le formulaire d'ajout (vide) et le
	  formulaire de saisie du nom. Si le formulaire `NameForm` est soumis en
	  GET (méthode="get" dans le template), le nom est utilisé pour
	  personnaliser le message.
	"""
	# Remplacer le message dépendant de l'heure par un message statique
	default_message = "Bonjour !"

	try:
		liste_taches = Tache.objects.order_by('titre')
	except Exception:
		liste_taches = []

	# Message statique (la personnalisation par nom a été retirée)
	message = default_message

	tache_form = TacheForm()

	context = {
		'message': message,
		'tache_form': tache_form,
		'taches': liste_taches,
	}

	return render(request, 'accueil.html', context)


def ajouter_tache(request):
	"""Gère uniquement l'ajout d'une nouvelle tâche (POST).

	En cas d'appel en GET ou autre méthode, redirige vers la vue de liste.
	"""
	if request.method != 'POST':
		return redirect('index')

	tache_form = TacheForm(request.POST)
	if tache_form.is_valid():
		tache_form.save()

	return redirect('index')
