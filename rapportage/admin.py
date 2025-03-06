from django.contrib import admin

from .models import RapportMensuel, RapportSemestriel, RapportTrimestriel, RapportAnnuel


@admin.register(RapportMensuel)
class RapportMensuelAdmin(admin.ModelAdmin):
    list_display = ('label', 'state',)
    list_filter = ('state',)


@admin.register(RapportTrimestriel)
class RapportTrimestrielAdmin(admin.ModelAdmin):
    list_display = ('label', 'state',)
    list_filter = ('state',)


@admin.register(RapportSemestriel)
class RapportSemestrielAdmin(admin.ModelAdmin):
    list_display = ('label', 'state',)
    list_filter = ('state',)


@admin.register(RapportAnnuel)
class RapportAnnuelAdmin(admin.ModelAdmin):
    list_display = ('label', 'state',)
    list_filter = ('state',)