from django.urls import path
from .views import PlanPTBAProjet

app_name = 'planification'
urlpatterns = [
    path('ptba-projet/', PlanPTBAProjet.as_view(), name='ptba-projet'),
]