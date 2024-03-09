from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Agriculteur, InformationAgricole, Prediction
from .forms import * 


from django.shortcuts import render
from .forms import InformationAgricoleForm

from joblib import load
model = load('./savedmodels/model.joblib')

def home(request):
    if request.method == 'POST':
        form = InformationAgricoleForm(request.POST)
        if form.is_valid():
            form.save()
            # Rediriger l'utilisateur vers une autre page ou afficher un message de succès
    else:
        form = InformationAgricoleForm()
    return render(request, 'home.html', {'form': form})

def agriculteurs_list(request):
    agriculteurs = Agriculteur.objects.all()
    return render(request, 'agriculteurs_list.html', {'agriculteurs': agriculteurs})

def agriculteur_detail(request, agriculteur_id):
    agriculteur = get_object_or_404(Agriculteur, id=agriculteur_id)
    informations = InformationAgricole.objects.filter(agriculteur=agriculteur)
    predictions = Prediction.objects.filter(agriculteur=agriculteur)
    return render(request, 'agriculteur_detail.html', {'agriculteur': agriculteur, 'informations': informations, 'predictions': predictions})

def information_create(request, agriculteur_id):
    agriculteur = get_object_or_404(Agriculteur, id=agriculteur_id)
    if request.method == 'POST':
        form = InformationAgricoleForm(request.POST)
        if form.is_valid():
            information = form.save(commit=False)
            information.agriculteur = agriculteur
            information.save()
            return redirect('agriculteur_detail', agriculteur_id=agriculteur.id)
    else:
        # Exclure le champ rendement du formulaire
        form = InformationAgricoleForm(exclude=['rendement'])
    return render(request, 'information_create.html', {'form': form})

def prediction_create(request, agriculteur_id):
    agriculteur = get_object_or_404(Agriculteur, id=agriculteur_id)
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            prediction = form.save(commit=False)
            prediction.agriculteur = agriculteur
            prediction.save()
            return redirect('agriculteur_detail', agriculteur_id=agriculteur.id)
    else:
        initial_data = {'nom': agriculteur.nom, 'email': agriculteur.email}
        form = PredictionForm(initial=initial_data)
    return render(request, 'prediction_create.html', {'form': form})