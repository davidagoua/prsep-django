from django.shortcuts import render
from django.views import generic



class ComposanteTemplateView(generic.TemplateView):
    template_name = 'settings/composantes.html'

    def get_context_data(self, **kwargs):

        return kwargs | locals()