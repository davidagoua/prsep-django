from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from programme.models import ComposantesProgram, DomainResult, SousDomainResult
from test import ingest


def ingest_data(request, sheet_name):
    response = ingest(sheet_name)
    return JsonResponse({'status': 'ok', 'data': response})


class SuiviTemplateView(generic.TemplateView):
    template_name = 'suivi/ptba-programme.html'

    def get_context_data(self, **kwargs):
        composants = ComposantesProgram.objects.all()
        domain_result = DomainResult.objects.all()
        souscomposants = SousDomainResult.objects.all()
        return kwargs | locals()