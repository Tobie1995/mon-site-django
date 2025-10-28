from django.shortcuts import render
from django.utils import timezone
from .forms import NameForm
from .models import Tache  # Importer le modèle Tache


def index(request):
	"""Affiche la page d'accueil avec un message selon l'heure et un formulaire de nom.

	- Avant midi : "Bon matin !"
	- Après midi : "Bon après-midi !"
	"""
	# Use Django timezone-aware local time so the greeting follows
	# the project's TIME_ZONE setting instead of the system local time.
	current_hour = timezone.localtime(timezone.now()).hour
	if current_hour < 12:
		default_message = "Bon matin !"
	else:
		default_message = "Bon après-midi"

	# Récupère toutes les tâches depuis la base de données, ordonnées par titre.
	# En cas d'erreur (par ex. base non migrée), on retourne une liste vide pour éviter une erreur 500.
	try:
		liste_taches = Tache.objects.order_by('titre')
	except Exception:
		liste_taches = []

	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			message = f"{default_message} {name} !"
		else:
			message = default_message
	else:
		form = NameForm()
		message = default_message

	context = {
		'message': message,
		'today': timezone.now().date(),
		'form': form,
		'taches': liste_taches,
	}

	return render(request, 'accueil.html', context)
