# urls.py

from django.urls import path
from . import views
from .views import home
from .views import inserer_donnees
 

urlpatterns = [
    
    path('', home, name='home'),
    path('agriculteurs/', views.agriculteurs_list, name='agriculteurs_list'),
    path('agriculteur/<int:agriculteur_id>/', views.agriculteur_detail, name='agriculteur_detail'),
    path('agriculteur/<int:agriculteur_id>/information/create/', views.information_create, name='information_create'),
    path('agriculteur/<int:agriculteur_id>/prediction/create/', views.prediction_create, name='prediction_create'),
    # Autres patterns d'URL
    path('inserer_donnees/', inserer_donnees, name='inserer_donnees'),
]
