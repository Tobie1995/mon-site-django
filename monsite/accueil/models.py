from django.db import models


# Modèle représentant une tâche simple
class Tache(models.Model):

	titre = models.CharField(max_length=200)
	termine = models.BooleanField(default=False)

	def __str__(self):
		return self.titre

