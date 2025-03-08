from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from planification.models import ILD, AppuiTechnique, Tache, PTBAProjet


class HomePageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):

        ptba = PTBAProjet.objects.first()

        return kwargs | {
            'nb_projects': Tache.objects.all().count() + AppuiTechnique.objects.all().count(),
            'nb_projects_pending': Tache.objects.filter(status=10).count() + AppuiTechnique.objects.filter(status=10).count(),
            'nb_projects_completed': Tache.objects.filter(status=500).count() + AppuiTechnique.objects.filter(status=500).count(),
            'nb_projects_upcoming': Tache.objects.filter(status=0).count() + AppuiTechnique.objects.filter(status=0).count(),
            'ptba': ptba,
        }


class CartigraphieView(LoginRequiredMixin, generic.TemplateView):
    template_name = "carto.html"


class AnalyseView(LoginRequiredMixin, generic.TemplateView):
    template_name = "analyse.html"