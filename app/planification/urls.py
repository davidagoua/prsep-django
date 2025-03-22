from django.urls import path
from .views import PlanPTBAProjet, TacheForm, PPMListView, TacheCreateFormView, tache_detail, PlanPTBAProgramme

app_name = 'planification'
urlpatterns = [
    path('ptba-projet/', PlanPTBAProjet.as_view(), name='ptba-projet'),
    path('ptba-programme/', PlanPTBAProgramme.as_view(), name='ptba-programme'),
    path('create-ild/', TacheCreateFormView.as_view(), name='create-ild'),
    path('ppm-list/', PPMListView.as_view(), name='ppm-list'),
    path('tache/<int:id>/', tache_detail, name='tache_detail'),


]