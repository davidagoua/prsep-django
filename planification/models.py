from datetime import date

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django_extensions.db.models import TimeStampedModel

from core.models import Departement


class PTBAProjet(TimeStampedModel, models.Model  ):
    montant_total = models.BigIntegerField(default=0)
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
    composant = models.ForeignKey(ComposantProjet, on_delete=models.CASCADE, related_name='souscomposants')
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.label)


class ILD(TimeStampedModel, models.Model):
    type = models.CharField(max_length=100, choices=models.TextChoices("type_composant",'ILD AT'), null=True, blank=True)
    label = models.CharField(max_length=100)
    sous_composant = models.ForeignKey(SousComposantProjet, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self): return str(self.label)


class CategorieDepense(TimeStampedModel, models.Model):
    label = models.CharField(max_length=100)
    status = models.IntegerField(default=0)


class Indicateur(TimeStampedModel, models.Model):
    type = models.CharField(max_length=100, choices=models.TextChoices("type_composant",(('ILD','Indicateur_Lie_Decaissement'), ('Appui Technique','Appui Technique'))), null=True, blank=True)
    label = models.CharField(max_length=100)
    sous_composant = models.ForeignKey(SousComposantProjet, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self): return str(self.label)

    class Meta:
        ordering = ('pk',)


class RLD(TimeStampedModel, models.Model):
    ild = models.ForeignKey(Indicateur, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.label)

class AppuiTechnique(TimeStampedModel, models.Model):
    label = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    sous_composant = models.ForeignKey(SousComposantProjet, on_delete=models.CASCADE)


    def __str__(self): return str(self.label)


class CategorieDepense(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return str(self.label)


class TypeUnite(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return str(self.label)


class TypeProcedureAcquisition(models.Model):
    label = models.CharField(max_length=100)


class Decaissement(TimeStampedModel, models.Model):
    montant = models.BigIntegerField(default=0)
    status = models.IntegerField(default=0)
    in_drf = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    tache = models.ForeignKey('Tache', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str('DRF:'+self.pk +self.montant)


class TypeUGP(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return str(self.label)


class TachePublicManager(models.Manager):

    def get_queryset(self):
        return Tache.objects.all()


class Tache(TimeStampedModel, models.Model):
    type = models.CharField(max_length=100, choices=models.TextChoices("type_composant",'RLD V'), null=True, blank=True)
    label = models.TextField()
    categorie = models.ForeignKey(CategorieDepense, on_delete=models.SET_NULL, null=True)
    indicateur = models.ForeignKey(Indicateur, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(default=0)
    unite = models.ForeignKey(TypeUnite, on_delete=models.CASCADE)
    montant_engage = models.PositiveBigIntegerField(default=0)
    cout = models.BigIntegerField(default=0)
    quantite = models.PositiveIntegerField(default=0)
    frequence = models.PositiveBigIntegerField(default=1)
    ugp = models.ForeignKey(TypeUGP, on_delete=models.SET_NULL, null=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    responsable = models.CharField(max_length=100, null=True, blank=True)
    depends_on = models.ManyToManyField('Tache', null=True, blank=True)
    departement = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True, blank=True)

    objects = models.Manager()
    public = TachePublicManager()

    def __str__(self): return str(self.label)

    @property
    def from_last_year(self) -> bool:
        return self.date_fin.year < date.today().year


class Activite(TimeStampedModel, models.Model):
    label = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    unite = models.CharField(max_length=100)
    montant_engage = models.PositiveBigIntegerField()
    cout = models.BigIntegerField(default=0)
    parent_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    parent_id = models.PositiveIntegerField()
    parent = GenericForeignKey('parent_type', 'parent_id')

    def __str__(self): return str(self.label)



class PPM(TimeStampedModel, models.Model):
    file = models.FileField(null=True, blank=True)
    label = models.CharField(max_length=100)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.label)



