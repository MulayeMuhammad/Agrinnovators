from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import Agriculteur, InformationAgricole, Prediction

admin.site.register(Agriculteur) 
admin.site.register(InformationAgricole)
admin.site.register(Prediction)
 
