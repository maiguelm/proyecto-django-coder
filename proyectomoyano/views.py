from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from proyectomoyano.models import Contacto, Vino
from proyectomoyano.forms import BuscarVino, ContactForm, CrearVinoForm


def inicio(request):  
    return render(request, 'proyectomoyano/index.html', {})

def about(request):
    return render(request, 'proyectomoyano/about.html', {})

@login_required
def wines(request):
    if request.method == 'POST':
        formulario = CrearVinoForm(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            etiqueta = (data_form.get('etiqueta')).lower()
            varietal = data_form.get('varietal')
            cosecha = data_form.get('cosecha')
            descripcion = (data_form.get('descripcion')).lower()
            tipo = data_form.get('tipo')
            imagen = data_form.get('imagen')
            fecha_compra = data_form.get('fecha_compra')

            cons_form = Vino(etiqueta=etiqueta, varietal=varietal, cosecha=cosecha, descripcion=descripcion, tipo=tipo, fecha_compra=fecha_compra)
            cons_form.save()
            return redirect('busquedavinos')
        else:
            return render(request, 'proyectomoyano/wines.html', {'formulario': formulario})
            
    formulario = CrearVinoForm()
    return render(request, 'proyectomoyano/wines.html', {'formulario': formulario})

def buscarVinos(request):
    formulario = BuscarVino(request.GET)
    if formulario.is_valid():
        vino_buscado = formulario.cleaned_data.get('etiqueta')
        listado_de_vinos = Vino.objects.filter(etiqueta__icontains=vino_buscado)
    
    formulario = BuscarVino()
    return render(request, 'proyectomoyano/busquedavinos.html', {'formulario': formulario, 'listado_de_vinos': listado_de_vinos})

class UpdateWine(LoginRequiredMixin, UpdateView):
    model = Vino
    template_name = "proyectomoyano/update_wine.html"
    fields = ['etiqueta', 'varietal', 'cosecha', 'descripcion', 'tipo', 'imagen', 'fecha_compra']
    success_url = reverse_lazy('busquedavinos')


class DetailWine(DetailView):
    model = Vino
    template_name = "proyectomoyano/detail_wine.html"
    
class DeletWine(LoginRequiredMixin, DeleteView):
    model = Vino
    template_name = "proyectomoyano/delete_wines.html"
    success_url = reverse_lazy('busquedavinos')


def contact(request):
    if request.method == 'POST':
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            nombre = data_form.get('nombre')
            mail = data_form.get('mail')
            phone = data_form.get('telefono')
            consulta = data_form.get('consulta')

            cons_form = Contacto(nombre=nombre.lower, mail=mail, telefono=phone, consulta=consulta.lower)
            cons_form.save()
            
        else:
                return render(request, 'proyectomoyano/contact.html', {'formulario': formulario})
            
    formulario = ContactForm()

    return render(request, 'proyectomoyano/contact.html', {'formulario': formulario})
