

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.shortcuts import render, redirect, reverse, resolve_url
from django.views import generic
from django.views.generic import FormView, ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectTemplateResponseMixin
from django.views.generic.edit import FormMixin, CreateView

from rapportage.forms import RapportForm
from rapportage.models import TypeRapport, Rapport



class RapportMensuelView(LoginRequiredMixin, FormView, MultipleObjectTemplateResponseMixin):
    template_name = 'rapportage/mensuel.html'
    form_class = RapportForm
    object_list = Rapport.objects.filter(type='Mensuel')

    def get_queryset(self):
        return Rapport.objects.filter(type='Mensuel')

    def get_context_data(self, **kwargs):
        return kwargs | {
            'object_list': self.object_list,
        }

    def form_valid(self, form):
        rapport = form.save(commit=False)
        rapport.user = self.request.user
        rapport.type = 'Mensuel'
        rapport.save()#save the object.
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return resolve_url('rapport:mensuel')


class RapportTrimestreView(generic.TemplateView):
    template_name = 'rapportage/trimestre.html'


class RapportSemestreView(generic.TemplateView):
    template_name = 'rapportage/semestre.html'


class RapportAnnuelView(generic.TemplateView):
    template_name = 'rapportage/annuel.html'


class RapportConsolideView(generic.TemplateView):
    template_name = 'rapportage/consolide.html'


def download_file(request, rapport):
    return FileResponse(open(rapport.file.path, 'rb'))

def upload_file(request, rapport):
    if request.method == 'POST':
        rapport.file = request.FILES['file']
    redirect(resolve_url('rapport:mensuel'))


def update_state(request, rapport):
    rapport.state = request.GET.get('state')
    rapport.save()
    return redirect('rapport:mensuel')