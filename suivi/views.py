from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils.timezone import now

from django.views import generic
from django.views.generic.detail import SingleObjectTemplateResponseMixin

from planification.forms import UpdateTacheForm, DecaissementFormSet
from planification.models import SousComposantProjet, ComposantProjet, Tache, Decaissement, Exercice


class SuiviPTBAProjetView(generic.TemplateView):
    template_name = 'suivi/ptba-projet.html'

    def get_context_data(self, **kwargs):

        return kwargs | {
            'updatetacheform': UpdateTacheForm,
            'composants': ComposantProjet.objects.all().order_by('pk'),
            'exercices': Exercice.objects.all(),
            'year': now().year
        }


class UpdateTacheView(SingleObjectTemplateResponseMixin, generic.FormView):
    form_class = UpdateTacheForm
    template_name = 'suivi/update_tache.html'

    def get_queryset(self):
        return Tache.objects.all()

    def get_context_data(self, **kwargs):
        object = Tache.objects.get(pk=self.kwargs['pk'])
        return kwargs | {
            'updatetacheform': UpdateTacheForm(instance=object),
            'object': object
        }





class AddDecaissementView(generic.DetailView):

    template_name = 'suivi/add-decaissement-projet.html'
    model = Tache

    def get_success_url(self):
        return resolve_url('suivi:add-decaissement-projet', pk=self.get_object().pk)

    def get_context_data(self, **kwargs):
        return kwargs | {

        }

    def post(self, request, *args, **kwargs):
        tache = self.get_object()
        try:
            montant_engage = int(request.POST.get('montant_engage'))
            paiement = int(request.POST.get('paiement'))

            if montant_engage < 0:
                raise ValueError("Le montant engagé ne peut pas être négatif.")

            if paiement > 0:
                Decaissement(montant=paiement, user=request.user, in_drf=True, tache=tache).save()

            tache.montant_engage = montant_engage
            tache.save()
            messages.success(request, "Le montant engagé a été mis à jour avec succès.")
            return redirect(self.get_success_url())
        except (ValueError, TypeError) as e:
            messages.error(request, e.__dict__)
            return redirect(self.get_success_url())
        except Exception as e:
            messages.error(request, f"Une erreur s'est produite: {e}")
            return redirect(self.get_success_url())


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


def delete_decaissement(request, pk):
    d = get_object_or_404(Decaissement, pk=pk)
    tache = d.tache
    d.delete()
    return redirect('suivi:add-decaissement-projet', pk=tache.pk)


def update_state(request, pk):
    tache = get_object_or_404(
        Tache,
        pk=pk)
    tache.status_execution = request.GET.get('status')
    tache.save()
    return redirect(resolve_url('plan:tache_detail', pk=tache.pk))

