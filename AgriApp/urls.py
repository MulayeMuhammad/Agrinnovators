# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('agriculteurs/', views.agriculteurs_list, name='agriculteurs_list'),
    path('agriculteur/<int:agriculteur_id>/', views.agriculteur_detail, name='agriculteur_detail'),
    path('agriculteur/<int:agriculteur_id>/information/create/', views.information_create, name='information_create'),
    path('agriculteur/<int:agriculteur_id>/prediction/create/', views.prediction_create, name='prediction_create'),
]
