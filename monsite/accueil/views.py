from django.http import HttpResponse


def bonjour(request):
	"""Vue minimale affichant le message de bienvenue."""
	return HttpResponse("Bonjour, le monde de Django !")
