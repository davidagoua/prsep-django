from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.shortcuts import render, redirect, reverse, resolve_url, get_object_or_404
from django.views import generic
from django.views.generic import FormView, ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectTemplateResponseMixin
from django.views.generic.edit import FormMixin, CreateView


from rapportage.forms import RapportForm
from rapportage.models import TypeRapport, Rapport



class RapportMensuelView(LoginRequiredMixin, FormView, ListView):
    template_name = 'rapportage/mensuel.html'
    form_class = RapportForm
    object_list = Rapport.objects.filter(type='Mensuel')

    def get_queryset(self):
        return Rapport.objects.filter(type='Mensuel')

    def form_valid(self, form):
        rapport = form.save(commit=False)
        rapport.user = self.request.user
        rapport.type = 'Mensuel'
        rapport.save()
        messages.success(self.request, "Rapport enregistré")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Le formulaire est invalide.")
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return resolve_url('rapport:rapport-mensuel')


class RapportTrimestreView(generic.TemplateView):
    template_name = 'rapportage/trimestre.html'


class RapportSemestreView(generic.TemplateView):
    template_name = 'rapportage/semestre.html'


class RapportAnnuelView(generic.TemplateView):
    template_name = 'rapportage/annuel.html'


class RapportConsolideView(generic.TemplateView):
    template_name = 'rapportage/consolide.html'


def download_file(request, pk):
    rapport = get_object_or_404(Rapport, id=pk)
    return FileResponse(open(rapport.file.path, 'rb'))


def upload_file(request, rapport):
    if request.method == 'POST':
        rapport.file = request.FILES['file']
    redirect(resolve_url('rapport:mensuel'))


def update_file_and_label(request, rapport_id):
    rapport = get_object_or_404(Rapport, id=rapport_id)
    if request.method == 'POST':
        rapport.file = request.FILES.get('file', rapport.file)
        rapport.label = request.POST.get('label', rapport.label)
        rapport.save()
        messages.success(request, "Le fichier et le libellé du rapport ont été mis à jour.")
    else:
        messages.error(request, "Aucune modification n'a été effectuée.")
    return redirect('rapport:mensuel')


def update_state(request, pk):
    rapport = get_object_or_404(
        Rapport,
        pk=request.GET.get('pk'))
    rapport.state = request.GET.get('state')
    rapport.save()
    return redirect('rapport:mensuel')

