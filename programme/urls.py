from django.urls import path

from programme.views import ingest_data, SuiviTemplateView

app_name = 'programme'
urlpatterns = [
    path('ingest/<str:sheet_name>', ingest_data),
    path('suivi-programme/', SuiviTemplateView.as_view(), name='suivi'),
]