from django.contrib import admin
from .models import PTBAProjet, ComposantProjet, SousComposantProjet, ILD, AppuiTechnique, Tache, Activite, RLD


@admin.register(PTBAProjet)
class PTBAProjetAdmin(admin.ModelAdmin):
    list_display = ('montant_total', 'created', 'modified')
    list_filter = ('created',)
    date_hierarchy = 'created'


@admin.register(ComposantProjet)
class ComposantProjetAdmin(admin.ModelAdmin):
    list_display = ('label', 'ptba', 'created')
    search_fields = ('label',)
    list_filter = ('ptba',)






@admin.register(SousComposantProjet)
class SousComposantProjetAdmin(admin.ModelAdmin):
    list_display = ('label', 'sigle', 'composant', 'created')
    search_fields = ('label', 'sigle')
    list_filter = ('composant',)



@admin.register(ILD)
class ILDAdmin(admin.ModelAdmin):
    list_display = ('label', 'sous_composant', 'created')
    search_fields = ('label',)
    list_filter = ('sous_composant',)
    fieldsets = (
        (None, {'fields': ('label', 'sous_composant', 'description')}),
    )


@admin.register(RLD)
class RLDAdmin(admin.ModelAdmin):
    list_display = ('label', 'ild', 'created')
    search_fields = ('label',)
    list_filter = ('ild',)
    fieldsets = (
        (None, {'fields': ('label', 'ild')}),
    )


@admin.register(AppuiTechnique)
class AppuiTechniqueAdmin(admin.ModelAdmin):
    list_display = ('label', 'sous_composant', 'created')
    search_fields = ('label',)
    list_filter = ('sous_composant',)
    fieldsets = (
        (None, {'fields': ('label', 'sous_composant', 'description')}),
    )


@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ('label', 'categorie', 'unite', 'montant_engage', 'parent', 'created')
    search_fields = ('label', 'categorie')
    list_filter = ('categorie', 'parent')
    fieldsets = ((
        (None, {'fields': ('label', 'categorie', 'unite', 'montant_engage', 'parent')}),
    ))



@admin.register(Activite)
class ActiviteAdmin(admin.ModelAdmin):
    list_display = ('label', 'categorie', 'unite', 'montant_engage', 'parent', 'created')
    search_fields = ('label', 'categorie')
    list_filter = ('categorie', 'parent')
    fieldsets = (
        (None, {'fields': ('label', 'categorie', 'unite', 'montant_engage', 'parent')}),
    )


