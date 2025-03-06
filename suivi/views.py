from django.shortcuts import render

from django.views import generic

from planification.models import SousComposantProjet, ComposantProjet


class SuiviPTBAProjetView(generic.TemplateView):
    template_name = 'suivi/ptba-projet.html'

    def get_context_data(self, **kwargs):

        return kwargs | {
            'composants': ComposantProjet.objects.all(),
        }
