from django.db import models

class Tache(models.Model):
	"""Représente une tâche (to-do) simple.

	Cette classe modèle stocke les informations minimales pour une tâche :
	son titre et son état d'achèvement.

	Attributes:
		titre (str): Le titre ou la description courte de la tâche (max 200 caractères).
		termine (bool): True si la tâche est complétée, False sinon. Valeur par défaut : False.

	La méthode __str__ renvoie le titre pour une représentation lisible dans l'admin
	et les interfaces Django.
	"""

	titre = models.CharField(max_length=200)
	termine = models.BooleanField(default=False)

	def __str__(self):
		"""Retourne une représentation lisible de la tâche.

		Returns:
			str: Le titre de la tâche.
		"""
		return self.titre

