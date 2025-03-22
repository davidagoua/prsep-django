from django.urls import path

from programme.views import ingest_data, SuiviTemplateView, ListTache, TDRProgramLocalListView, \
    TDRProgramTechniqueListView, TDRProgramCoordListView

app_name = 'programme'
urlpatterns = [
    path('ingest/<str:sheet_name>', ingest_data),
    path('suivi-programme/', SuiviTemplateView.as_view(), name='suivi'),
    path('liste-programme/', ListTache.as_view(), name='liste-tache'),
    path('liste-programme-direction-local/', TDRProgramLocalListView.as_view(), name='liste-tache-local'),
    path('liste-programme-direction-technique/', TDRProgramTechniqueListView.as_view(), name='tdr_technique'),
    path('liste-programme-direction-coord/', TDRProgramCoordListView.as_view(), name='tdr_coord'),
]