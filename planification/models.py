from datetime import date

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Sum
from django.utils.timezone import now
from django_extensions.db.models import TimeStampedModel

from core.models import Departement, User



class PTBAProjet(TimeStampedModel, models.Model  ):
    montant_total = models.BigIntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str('ptba project '+self.created.__str__())

    @property
    def montant_planifier(self) -> int:
        return sum(composant.montant_planifier for composant in self.composantprojet_set.all())

    @property
    def montant_engage(self) -> int:
        return sum(composant.montant_engage for composant in self.composantprojet_set.all())

    @property
    def somme_drf(self) -> int:
        return sum(composant.somme_drf for composant in self.composantprojet_set.all())

    @property
    def reste_a_payer(self) -> int:
        return self.montant_engage - self.somme_drf

    @property
    def reste_a_planifier(self) -> int:
        return self.montant_total - self.montant_engage

    


class ComposantProjet(TimeStampedModel, models.Model):
    label = models.CharField(max_length=100)
    ptba = models.ForeignKey(PTBAProjet, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)


    @property
    def montant_planifier(self) -> int:
        return sum(sous_composant.montant_planifier for sous_composant in self.souscomposants.all())

    @property
    def montant_engage(self) -> int:
        return sum(sous_composant.montant_engage for sous_composant in self.souscomposants.all())

    @property
    def somme_drf(self) -> int:
        return sum(sous_composant.somme_drf for sous_composant in self.souscomposants.all())

    @property
    def reste_a_payer(self) -> int:
        return self.montant_engage - self.somme_drf

    def __str__(self):
        return str(self.label)


class SousComposantProjet(TimeStampedModel, models.Model):
    label = models.CharField(max_length=100)
    sigle = models.CharField(max_length=100, null=True, blank=True)
    composant = models.ForeignKey(ComposantProjet, on_delete=models.CASCADE, related_name='souscomposants')
    status = models.IntegerField(default=0)

    @property
    def montant_planifier(self) -> int:
        return sum(indicateur.montant_planifier for indicateur in self.indicateur_set.all())

    @property
    def montant_engage(self) -> int:
        return sum(indicateur.montant_engage for indicateur in self.indicateur_set.all())

    @property
    def somme_drf(self) -> int:
        return sum(
            tache.total_decaissement for indicateur in self.indicateur_set.all() for tache in indicateur.tache_set.all()
        )

    @property
    def reste_a_payer(self) -> int:
        return self.montant_engage - self.somme_drf

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
    type = models.CharField(max_length=100, choices=models.TextChoices("type_composant",(('ILD','ILD'), ('HORS_ILD','HORS ILD'))), null=True, blank=True)
    label = models.CharField(max_length=100)
    sous_composant = models.ForeignKey(SousComposantProjet, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self): return str(self.label)

    @property
    def montant_planifier(self) -> int:
        return sum(tache.montant_planifier for tache in self.tache_set.all())


    @property
    def montant_engage(self) -> int:
        return sum(tache.montant_engage for tache in self.tache_set.all())

    @property
    def somme_drf(self) -> int:
        return sum(tache.total_decaissement for tache in self.tache_set.all())

    @property
    def reste_a_payer(self) -> int:
        return self.montant_engage - self.somme_drf

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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'DRF:{self.pk} {self.montant}'


class TypeUGP(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return str(self.label)


class TachePublicManager(models.Manager):

    def get_queryset(self):
        return Tache.objects.all()


class Tache(TimeStampedModel, models.Model):
    type = models.CharField(max_length=100, choices=models.TextChoices("type_composant",'RLD HORS_RLD'), null=True, blank=True)
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
    status_validation = models.PositiveSmallIntegerField(default=0)

    objects = models.Manager()
    public = TachePublicManager()

    def __str__(self): return str(self.label)

    @property
    def from_last_year(self) -> bool:
        return self.date_fin.year < date.today().year

    @property
    def montant_planifier(self) -> int:
        return self.frequence * self.quantite * self.cout

    @property
    def total_decaissement(self) -> int:
        result = self.decaissement_set.aggregate(total=Sum('montant'))
        return result['total'] or 0

    @property
    def reste_paye(self) -> int:
        return self.montant_engage - self.total_decaissement


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



