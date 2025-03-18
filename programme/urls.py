from django.urls import path

from programme.views import ingest_data

app_name = 'programme'
urlpatterns = [
    path('ingest/<str:sheet_name>', ingest_data)
]