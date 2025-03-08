from django.urls import path

from rapportage.views import (RapportMensuelView, update_state,
                              RapportAnnuelView, RapportSemestreView, RapportConsolideView, RapportTrimestreView)

app_name = "analyse"
urlpatterns = [
    path('rapport-mensuel/', RapportMensuelView.as_view(), name='rapport-mensuel'),
    path('rapport-trimestriel/', RapportTrimestreView.as_view(), name='rapport-trimestriel'),
    path('rapport-semestriel/', RapportSemestreView.as_view(), name='rapport-semestriel'),
    path('rapport-annuel/', RapportAnnuelView.as_view(), name='rapport-annuel'),
    path('rapport-consolide/', RapportConsolideView.as_view(), name='rapport-consolide'),
    path('update-state/<int:pk>', update_state, name='update_state'),
]