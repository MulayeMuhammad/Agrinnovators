# forms.py

from django import forms
from .models import InformationAgricole, Prediction

class InformationAgricoleForm(forms.ModelForm):
    class Meta:
        model = InformationAgricole
        fields = ['superficie', 'region', 'capital', 'travailleurs', 'humidite', 'temperature', 'rendement', 'produit', 'prix_produit']
class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields =  '__all__'



