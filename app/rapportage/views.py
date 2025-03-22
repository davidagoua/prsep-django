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


class RapportTrimestreView(LoginRequiredMixin, FormView, ListView):
    template_name = 'rapportage/trimestre.html'
    form_class = RapportForm
    object_list = Rapport.objects.filter(type='Trimestriel')

    def get_queryset(self):
        return Rapport.objects.filter(type='Trimestriel')

    def form_valid(self, form):
        rapport = form.save(commit=False)
        rapport.user = self.request.user
        rapport.type = 'Trimestriel'
        rapport.save()
        messages.success(self.request, "Rapport enregistré")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Le formulaire est invalide.")
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return resolve_url('rapport:rapport-trimestriel')


class RapportSemestreView(LoginRequiredMixin, FormView, ListView):
    template_name = 'rapportage/semestre.html'
    form_class = RapportForm
    object_list = Rapport.objects.filter(type='Semestriel')

    def get_queryset(self):
        return Rapport.objects.filter(type='Semestriel')

    def form_valid(self, form):
        rapport = form.save(commit=False)
        rapport.user = self.request.user
        rapport.type = 'Semestriel'
        rapport.save()
        messages.success(self.request, "Rapport enregistré")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Le formulaire est invalide.")
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return resolve_url('rapport:rapport-semestriel')


class RapportAnnuelView(LoginRequiredMixin, FormView, ListView):
    template_name = 'rapportage/annuel.html'
    form_class = RapportForm
    object_list = Rapport.objects.filter(type='Annuel')

    def get_queryset(self):
        return Rapport.objects.filter(type='Annuel')

    def form_valid(self, form):
        rapport = form.save(commit=False)
        rapport.user = self.request.user
        rapport.type = 'Annuel'
        rapport.save()
        messages.success(self.request, "Rapport enregistré")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Le formulaire est invalide.")
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return resolve_url('rapport:rapport-annuel')


class RapportConsolideView(LoginRequiredMixin, FormView, ListView):
    template_name = 'rapportage/consolide.html'
    form_class = RapportForm
    object_list = Rapport.objects.filter(type='Consolide')

    def get_queryset(self):
        return Rapport.objects.filter(type='Consolide')

    def form_valid(self, form):
        rapport = form.save(commit=False)
        rapport.user = self.request.user
        rapport.type = 'Consolide'
        rapport.save()
        messages.success(self.request, "Rapport enregistré")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Le formulaire est invalide.")
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return resolve_url('rapport:rapport-consolide')


def download_file(request, pk):
    rapport = get_object_or_404(Rapport, id=pk)
    return FileResponse(open(rapport.file.path, 'rb'))


def upload_file(request, pk):
    if request.method == 'POST':
        rapport = get_object_or_404(Rapport, id=pk)
        rapport.file = request.FILES['fichier']
        messages.success(request, "Fichier enregistré")
    return redirect(resolve_url('rapport:rapport-mensuel'))


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
        pk=pk)
    rapport.state = request.GET.get('status')
    rapport.save()
    return redirect(f'rapport:rapport-{ str(rapport.type).lower()}')

