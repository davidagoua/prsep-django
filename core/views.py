from django.shortcuts import render
from django.views import generic

from planification.models import ILD, AppuiTechnique


class HomePageView(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        return kwargs | {
            'nb_projects': ILD.objects.all().count() + AppuiTechnique.objects.all().count(),
            'nb_projects_pending': ILD.objects.filter(status=10).count() + AppuiTechnique.objects.filter(status=10).count(),
            'nb_projects_completed': ILD.objects.filter(status=500).count() + AppuiTechnique.objects.filter(status=500).count(),
            'nb_projects_upcoming': ILD.objects.filter(status=0).count() + AppuiTechnique.objects.filter(status=0).count(),
        }


class CartigraphieView(generic.TemplateView):
    template_name = "carto.html"


class AnalyseView(generic.TemplateView):
    template_name = "analyse.html"