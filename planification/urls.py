from django.urls import path
from .views import PlanPTBAProjet, TacheForm, PPMListView, TacheCreateFormView

app_name = 'planification'
urlpatterns = [
    path('ptba-projet/', PlanPTBAProjet.as_view(), name='ptba-projet'),
    path('create-ild/', TacheCreateFormView.as_view(), name='create-ild'),
    path('ppm-list/', PPMListView.as_view(), name='ppm-list'),
]