from django import forms


class NameForm(forms.Form):
    """Formulaire simple pour demander le nom de l'utilisateur."""
    name = forms.CharField(label='Votre nom', max_length=100, required=True)