from django.db import models

class Agriculteur(models.Model):
    nom = models.CharField(max_length=100)
    identifiant = models.CharField(max_length=100)  # Peut-être un champ UUIDField serait mieux
    email = models.EmailField()

    def __str__(self):
        return self.nom

class InformationAgricole(models.Model):
    agriculteur = models.ForeignKey(Agriculteur, on_delete=models.CASCADE)
    superficie = models.FloatField()
    region = models.CharField(max_length=100)
    capital = models.FloatField()
    humidite = models.FloatField()
    temperature = models.FloatField()
    qualite_sol = models.CharField(max_length=100)
    rendement = models.FloatField()
    produit = models.CharField(max_length=100)
    prix_produit = models.FloatField()

    def __str__(self):
        return f"{self.agriculteur.nom} - {self.region}"

class Prediction(models.Model):
    agriculteur = models.ForeignKey(Agriculteur, on_delete=models.CASCADE)
    date_prediction = models.DateField(auto_now_add=True)
    rendement_predit = models.FloatField()
    prix_predit = models.FloatField()

    def __str__(self):
        return f"Prédiction pour {self.agriculteur.nom} - {self.date_prediction}"