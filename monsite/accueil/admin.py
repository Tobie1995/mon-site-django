from django.contrib import admin
from .models import Tache  # Importer le modèle


@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
	list_display = ('titre', 'termine')
	list_filter = ('termine',)
	search_fields = ('titre',)
