from django.shortcuts import render
from django.utils import timezone
from .forms import NameForm


def index(request):
	default_message = "Bonjour, le monde de Django !"

	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			message = f"Bonjour, {name} !"
		else:
			message = default_message
	else:
		form = NameForm()
		message = default_message

	context = {
		'message': message,
		'today': timezone.now().date(),
		'form': form,
	}

	return render(request, 'accueil.html', context)
