from django.shortcuts import render
from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = "home.html"


class CartigraphieView(generic.TemplateView):
    template_name = "carto.html"


class AnalyseView(generic.TemplateView):
    template_name = "analyse.html"