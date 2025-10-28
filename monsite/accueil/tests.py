from django.test import TestCase
from .models import Tache


class TacheModelTest(TestCase):

	def test_str_returns_titre(self):
		titre = "Ma tâche de test"
		tache = Tache.objects.create(titre=titre)
		self.assertEqual(str(tache), titre)
