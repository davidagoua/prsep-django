from typing import override
from django.db import models



class Vehicule(models.Model):
    model = models.CharField(max_length=100)
    annee = models.IntegerField()
    marque = models.CharField(max_length=100)
    immatriculation = models.CharField(max_length=100)
    numero_chassis = models.CharField(max_length=100)
    entretients = models.JSONField()

    @override
    def __str__(self) -> str:
        return f'{self.marque} {self.model} {self.annee}'



class EmpruntVehicule(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_sortie = models.DateTimeField()
    date_retour = models.DateTimeField(null=True, blank=True)
    nom_prenom = models.CharField(max_length=100)
    nom_chauffeur = models.CharField(max_length=100)
    mission = models.TextField()
    km_in = models.PositiveIntegerField(default=0)
    km_out = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=100, default='En poul')
    is_panne = models.BooleanField(default=False)
    type_panne = models.CharField(max_length=100, null=True, blank=True)

    @override
    def __str__(self) -> str:
        return f"{self.vehicule} - {self.nom_prenom} - {self.nom_chauffeur} - {self.mission} - {self.date_sortie} - {self.date_retour}"
