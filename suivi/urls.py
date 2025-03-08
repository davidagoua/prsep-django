from django.urls import path

from suivi.views import SuiviPTBAProjetView, UpdateTacheView, ajouter_decaissements, AddDecaissementView, \
    delete_decaissement

app_name = 'suivi'

urlpatterns = [
    path('ptba-projet', SuiviPTBAProjetView.as_view(), name='ptba-projet'),
    path('update-tache/<int:pk>', ajouter_decaissements, name='update_tache'),
    path('add-decaissement-projet/<int:pk>', AddDecaissementView.as_view(), name='add-decaissement-projet'),
    path('delete-decaissement/<int:pk>', delete_decaissement, name='delete-decaissement'),
]