from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from programme.models import ComposantesProgram, DomainResult, SousDomainResult, TacheProgram
from suivi.models import TDRProgramme
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


class ListTache(generic.ListView):
    template_name = 'programme/liste_tache.html'

    def get_queryset(self):
        return TacheProgram.objects.all()



class TDRProgramLocalListView(LoginRequiredMixin, generic.ListView):
    template_name = "programme/local_list_activities.html"

    def get_queryset(self):
        return TacheProgram.objects.filter(
         Q(pk__in=[tdr.activity.pk for tdr in TDRProgramme.objects.filter(state=10)])
    )

    def get_context_data(
        self,**kwargs
    ):
        object_list = self.get_queryset()
        state = 20
        return kwargs | locals()

class TDRProgramTechniqueListView(LoginRequiredMixin, generic.ListView):
    template_name = "programme/local_list_activities.html"

    def get_queryset(self):
        return TacheProgram.objects.filter(
         Q(pk__in=[tdr.activity.pk for tdr in TDRProgramme.objects.filter(state=20)])
    )

    def get_context_data(
        self,**kwargs
    ):
        object_list = self.get_queryset()
        state = 30
        return kwargs | locals()


class TDRProgramCoordListView(LoginRequiredMixin, generic.ListView):
    template_name = "programme/local_list_activities.html"

    def get_queryset(self):
        return TacheProgram.objects.filter(
         Q(pk__in=[tdr.activity.pk for tdr in TDRProgramme.objects.filter(state__gte=20)])
    )

    def get_context_data(
        self,**kwargs
    ):
        state = 40
        object_list = self.get_queryset()
        return kwargs | locals()


class PTPAProgrammeStatsView(views.View):
    def get(self, request, *args, **kwargs):
        stats = TDRProgramme.objects.values('state').annotate(count=Count('state'))
        result = {item['state']: item['count'] for item in stats}
        result['pointFocal'] = TacheProgram.objects.filter(
            Q(pk__in=[tdr.activity.pk for tdr in TDRProgramme.objects.filter(state=0)])
        ).count()
        return JsonResponse(result)