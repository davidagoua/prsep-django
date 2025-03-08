from django.shortcuts import render, get_object_or_404, redirect

from django.views import generic

from planification.forms import UpdateTacheForm, DecaissementFormSet
from planification.models import SousComposantProjet, ComposantProjet, Tache


class SuiviPTBAProjetView(generic.TemplateView):
    template_name = 'suivi/ptba-projet.html'

    def get_context_data(self, **kwargs):

        return kwargs | {
            'updatetacheform': UpdateTacheForm,
            'composants': ComposantProjet.objects.all().order_by('pk'),
        }


class UpdateTacheView(generic.UpdateView):
    form_class = UpdateTacheForm

    def get_context_data(self, **kwargs):
        return kwargs | {
            'updatetacheform': UpdateTacheForm,
        }


def ajouter_decaissements(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    if request.method == 'POST':
        formset = DecaissementFormSet(request.POST, instance=tache)
        if formset.is_valid():
            formset.save()
            return redirect('nom_de_votre_vue_liste_taches')  # Redirige vers la liste des tâches
    else:
        formset = DecaissementFormSet(instance=tache)
    return render(request, 'ajouter_decaissements.html', {'formset': formset, 'tache': tache})