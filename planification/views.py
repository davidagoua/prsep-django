from django.shortcuts import render, resolve_url
from django.views import generic

from planification.forms import IldCreateForm
from planification.models import ILD, PPM


class PlanPTBAProjet(generic.TemplateView):
    template_name = 'plan/ptba-projet.html'

    def get_context_data(self, **kwargs):
        return kwargs | {
            'IldCreateForm': IldCreateForm,
            'ilds': ILD.objects.all(),
        }


class ILDCreateView(generic.FormView):
    form_class = IldCreateForm

    def form_valid(self, form):
        ild = form.save(commit=False)
        ild.user = self.request.user
        ild.save()
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url('plan:ptba-projet')


class PPMListView(generic.ListView):
    template_name = 'plan/ppm.html'
    queryset = PPM.objects.all()

