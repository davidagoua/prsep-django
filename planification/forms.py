from django import forms
from .models import ILD


class IldCreateForm(forms.ModelForm):
    class Meta:
        model = ILD
        exclude = ('user','status')