from django.urls import path

from suivi.views import SuiviPTBAProjetView

app_name = 'suivi'

urlpatterns = [
    path('/ptba-projet', SuiviPTBAProjetView.as_view(), name='ptba-projet'),
]