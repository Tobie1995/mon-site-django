from django.shortcuts import render
from django.utils import timezone
from .forms import NameForm


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

	tasks = [
		"Acheter du pain",
		"Envoyer l'email au client",
		"Apprendre Django: créer une vue",
		"Faire les tests unitaires"
	]

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
		'tasks': tasks,
	}

	return render(request, 'accueil.html', context)
