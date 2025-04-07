from django import forms
from .models import Vehicule, EmpruntVehicule

class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = '__all__'
        widgets = {
            'entretients': forms.Textarea(attrs={'rows': 4}),
        }

class EmpruntVehiculeForm(forms.ModelForm):
    class Meta:
        model = EmpruntVehicule
        fields = '__all__'
        widgets = {
            'date_sortie': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_retour': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'mission': forms.Textarea(attrs={'rows': 4}),
        }