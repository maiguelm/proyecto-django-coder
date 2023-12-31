from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from whiskies.models import Whisky
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class Whiskies(ListView):
    model = Whisky
    context_object_name = 'listado_de_whisky'
    template_name = 'whiskies/find_whisky.html'
    
    def get_queryset(self):
        etiqueta = self.request.GET.get('etiqueta', '')
        if etiqueta:
            listado_de_whisky = self.model.objects.filter(etiqueta__icontains=etiqueta)
        else:
            listado_de_whisky = self.model.objects.all()
        return listado_de_whisky


class CreateWhisky(LoginRequiredMixin, CreateView):
    model = Whisky
    template_name = "whiskies/whiskies.html"
    fields = ['etiqueta', 'aniejamiento', 'descripcion', 'tipo', 'fecha_compra', 'imagen']
    success_url = reverse_lazy('find_whisky')


class UpdateWhisky(LoginRequiredMixin, UpdateView):
    model = Whisky
    template_name = "whiskies/update_whiskies.html"
    fields = ['etiqueta', 'aniejamiento', 'descripcion', 'tipo', 'fecha_compra', 'imagen']
    success_url = reverse_lazy('find_whisky')

class DetailWhisky(DetailView):
    model = Whisky
    template_name = "whiskies/detail_whiskies.html"


class DeleteWhisky(LoginRequiredMixin, DeleteView):
    model = Whisky
    template_name = "whiskies/delete_whiskies.html"
    success_url = reverse_lazy('find_whisky')