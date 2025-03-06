from django import forms

from rapportage.models import RapportMensuel, RapportAnnuel, RapportSemestriel, RapportTrimestriel


class RapportMensuelForm(forms.ModelForm):

    class Meta:
        model = RapportMensuel
        exclude = ('user',)


class RapportTrimestrielForm(forms.ModelForm):

    class Meta:
        model = RapportTrimestriel
        exclude = ('user',)


class RapportSemestrielForm(forms.ModelForm):

    class Meta:
        model = RapportSemestriel
        exclude = ('user',)


class RapportAnnuelForm(forms.ModelForm):

    class Meta:
        model = RapportAnnuel
        exclude = ('user',)

