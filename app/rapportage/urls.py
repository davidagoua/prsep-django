from django.urls import path

from rapportage.views import (RapportMensuelView, update_state,upload_file,
                              RapportAnnuelView, RapportSemestreView, RapportConsolideView, RapportTrimestreView)
from rapportage.views import update_file_and_label, download_file

app_name = "analyse"
urlpatterns = [
    path('rapport-mensuel/', RapportMensuelView.as_view(), name='rapport-mensuel'),
    path('rapport-trimestriel/', RapportTrimestreView.as_view(), name='rapport-trimestriel'),
    path('rapport-semestriel/', RapportSemestreView.as_view(), name='rapport-semestriel'),
    path('rapport-annuel/', RapportAnnuelView.as_view(), name='rapport-annuel'),
    path('rapport-consolide/', RapportConsolideView.as_view(), name='rapport-consolide'),
    path('update-state/<int:pk>', update_state, name='update_state'),
    path('upload-file/<int:pk>', upload_file, name='upload_file'),
    path('update-file-and-label/<int:pk>', update_file_and_label, name='update_file_and_label'),
    path('download-file/<int:pk>', download_file, name='download_file'),
]