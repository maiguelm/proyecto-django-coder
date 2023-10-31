from django.shortcuts import render, redirect
from django.db.models import Q
from proyectomoyano.models import Contacto, Vino, Whisky
from proyectomoyano.forms import BuscarVino, ContactForm, CrearVinoForm, CrearWhiskyForm, BuscarWhisky


def inicio(request):  
    return render(request, 'proyectomoyano/index.html', {})

def about(request):
    return render(request, 'proyectomoyano/about.html', {})

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

            cons_form = Vino(etiqueta=etiqueta, varietal=varietal, cosecha=cosecha, descripcion=descripcion, tipo=tipo)
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


# def buscarVinos(request):
#     formulario = BuscarVino(request.GET)
#     busqueda_vino = request.GET.get("etiqueta")

#     if busqueda_vino:
#         listado_de_vinos = Vino.objects.filter(etiqueta__icontains=busqueda_vino)
#     else:
#         listado_de_vinos = Vino.objects.all()

#     return render(request, 'proyectomoyano/busquedavinos.html', {'formulario': formulario, 'listado_de_vinos': listado_de_vinos})


def whiskies(request):
    if request.method == 'POST':
       formulario = CrearWhiskyForm(request.POST)
       if formulario.is_valid():
           data_form = formulario.cleaned_data
           etiqueta = (data_form.get('etiqueta')).lower()
           aniejamiento = data_form.get('aniejamiento')
           descripcion = (data_form.get('descripcion')).lower()
           tipo = data_form.get('tipo')

           cons_form = Whisky(etiqueta=etiqueta, aniejamiento=aniejamiento, descripcion=descripcion, tipo=tipo)
           cons_form.save()
       else:
           return render(request, 'proyectomoyano/whiskies.html', {'formulario': formulario})
       
    formulario = CrearWhiskyForm()
    return render(request, 'proyectomoyano/whiskies.html', {'formulario': formulario})

# def buscarWhisky(request):
#     busqueda_whisky = request.GET.get("etiqueta")
#     if busqueda_whisky:
#         listado_de_whisky = Whisky.objects.filter(etiqueta__icontains=busqueda_whisky)
#     else:
#         listado_de_whisky = Whisky.objects.all()

#     return render(request, 'proyectomoyano/busquedavinos.html', {'listado_de_whisky': listado_de_whisky})

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
