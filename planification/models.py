from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django_extensions.db.models import TimeStampedModel



class PTBAProjet(TimeStampedModel, models.Model  ):
    montant_total = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str('ptba project '+self.created.__str__())


class ComposantProjet(TimeStampedModel, models.Model):
    label = models.CharField(max_length=100)
    ptba = models.ForeignKey(PTBAProjet, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.label)


class SousComposantProjet(TimeStampedModel, models.Model):
    label = models.CharField(max_length=100)
    sigle = models.CharField(max_length=100, null=True, blank=True)
    composant = models.ForeignKey(ComposantProjet, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.label)


class ILD(TimeStampedModel, models.Model):
    label = models.CharField(max_length=100)
    sous_composant = models.ForeignKey(SousComposantProjet, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self): return str(self.label)


class RLD(TimeStampedModel, models.Model):
    ild = models.ForeignKey(ILD, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.label)

class AppuiTechnique(TimeStampedModel, models.Model):
    label = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    sous_composant = models.ForeignKey(SousComposantProjet, on_delete=models.CASCADE)

    def __str__(self): return str(self.label)


class Tache(TimeStampedModel, models.Model):
    label = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    unite = models.CharField(max_length=100)
    montant_engage = models.DecimalField(decimal_places=2, max_digits=10)
    parent_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    parent_id = models.PositiveIntegerField()
    parent = GenericForeignKey('parent_type', 'parent_id')

    def __str__(self): return str(self.label)


class Activite(TimeStampedModel, models.Model):
    label = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    unite = models.CharField(max_length=100)
    montant_engage = models.DecimalField(decimal_places=2, max_digits=10)
    parent_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    parent_id = models.PositiveIntegerField()
    parent = GenericForeignKey('parent_type', 'parent_id')

    def __str__(self): return str(self.label)
