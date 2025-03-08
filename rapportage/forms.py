from django import forms

from rapportage.models import Rapport


class RapportForm(forms.ModelForm):

    class Meta:
        model = Rapport
        exclude = ('user','state','type')

