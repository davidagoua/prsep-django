from django.urls import path

from suivi.views import SuiviPTBAProjetView, UpdateTacheView, ajouter_decaissements, AddDecaissementView, \
    delete_decaissement, update_state, ActivitiesListView, CreateTDRView, update_tdr_state, delete_tdr, \
    TDRLocalListView, TDRTechniqueListView, download_tdr, TDRCoordinationListView, get_tdr_stats, cancel_tdr

app_name = 'suivi'

urlpatterns = [
    path('ptba-projet', SuiviPTBAProjetView.as_view(), name='ptba-projet'),
    path('update-tache/<int:pk>', UpdateTacheView.as_view(), name='update_tache'),
    path('add-decaissement-projet/<int:pk>', AddDecaissementView.as_view(), name='add-decaissement-projet'),
    path('delete-decaissement/<int:pk>', delete_decaissement, name='delete-decaissement'),
    path('update-state/<int:pk>', update_state, name='update_state'),
    path('activites/', ActivitiesListView.as_view(), name='list_activities'),
    path('tdr/create', CreateTDRView.as_view(), name='create_tdr'),
    path('update-tdr-state/<int:pk>/', update_tdr_state, name='update-tdr-state'),
    path('tdr/<int:pk>/delete', delete_tdr, name='delete_tdr'),
    path('tdr-local/', TDRLocalListView.as_view(), name='tdr_local'),
    path('tdr-technique/', TDRTechniqueListView.as_view(), name='tdr_technique'),
    path('tdr-coordination/', TDRCoordinationListView.as_view(), name='tdr_coordination'),
    path('tdr-download/<int:pk>', download_tdr, name='tdr_download'),
    path('tdr-get-stats', get_tdr_stats, name='get_tdr_stats'),
    path('tdr-cancel/<int:pk>', cancel_tdr, name='cancel_tdr'),
]