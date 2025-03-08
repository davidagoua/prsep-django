from django.urls import path

from suivi.views import SuiviPTBAProjetView, UpdateTacheView, ajouter_decaissements

app_name = 'suivi'

urlpatterns = [
    path('ptba-projet', SuiviPTBAProjetView.as_view(), name='ptba-projet'),
    path('update-tache/<int:pk>', ajouter_decaissements, name='update_tache'),
]