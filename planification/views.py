from django.shortcuts import render, resolve_url
from django.views import generic

from planification.forms import IldCreateForm, TacheForm
from planification.models import ILD, PPM, Tache


class PlanPTBAProjet(generic.TemplateView):
    template_name = 'plan/ptba-projet.html'

    def get_queryset(self):
        return Tache.objects.all()

    def get_context_data(self, **kwargs):
        return kwargs | {
            'IldCreateForm': TacheForm,
            'activites': Tache.objects.all(),
        }

    def get(self, request, *args, **kwargs):
        if (action := request.GET.get('action', None)) is not None:
            if action == 'soumettre':
                self.get_queryset().update(status_validation=request.GET.get('status', 10))
        return super().get(request, *args, **kwargs)


class TacheCreateFormView(generic.FormView):
    form_class = TacheForm

    def form_valid(self, form):
        activite = form.save(commit=False)
        activite.user = self.request.user
        activite.departement = self.request.user.departement
        activite.save()
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url('plan:ptba-projet')


class PPMListView(generic.ListView):
    template_name = 'plan/ppm.html'
    queryset = PPM.objects.all()

