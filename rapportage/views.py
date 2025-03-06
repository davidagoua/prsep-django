from django.shortcuts import render
from django.views import generic


class RapporMensuelForm:
    pass


class RapportMensuelView(generic.TemplateView):
    template_name = 'rapportage/mensuel.html'

    def get_context_data(self, **kwargs):
        return kwargs | {
            'create_form': RapporMensuelForm
        }


class RapportTrimestreView(generic.TemplateView):
    template_name = 'rapportage/trimestre.html'


class RapportSemestreView(generic.TemplateView):
    template_name = 'rapportage/semestre.html'


class RapportAnnuelView(generic.TemplateView):
    template_name = 'rapportage/annuel.html'


class RapportConsolideView(generic.TemplateView):
    template_name = 'rapportage/consolide.html'
