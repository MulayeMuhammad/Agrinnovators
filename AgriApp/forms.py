# forms.py

from django import forms
from .models import InformationAgricole, Prediction

class InformationAgricoleForm(forms.ModelForm):
    class Meta:
        model = InformationAgricole
        fields = ['superficie', 'region', 'prix_materiel', 'humidite', 'temperature', 'qualite_sol', 'rendement', 'produit', 'prix_produit']

class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ['date_prediction', 'rendement_predi', 'prix_predi']
