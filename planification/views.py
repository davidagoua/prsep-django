from django.shortcuts import render
from django.views import generic



class PlanPTBAProjet(generic.TemplateView):
    template_name = 'plan/ptba-projet.html'