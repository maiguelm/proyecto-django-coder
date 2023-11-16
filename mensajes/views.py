from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from mensajes.forms import MensajeForm

from mensajes.models import Mensaje



@login_required
def lista_mensajes(request):
    mensajes_enviados = Mensaje.objects.filter(remitente=request.user)
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    
    return render(request, 'mensajes/lista_mensajes.html', {
        'mensajes_enviados': mensajes_enviados,
        'mensajes_recibidos': mensajes_recibidos
    })


@login_required
def enviar_mensaje(request, destinatario_id):
    destinatario = get_object_or_404(User, id=destinatario_id)

    if request.method == 'POST':
        form = MensajeForm(request.POST, user=request.user)  
        if form.is_valid():
            contenido = form.cleaned_data['contenido']
            Mensaje.objects.create(remitente=request.user, destinatario=destinatario, contenido=contenido)
            return redirect('ver_conversacion', destinatario_id=destinatario_id)
    else:
        form = MensajeForm(user=request.user)  

    return render(request, 'mensajes/enviar_mensaje.html', {'destinatario': destinatario, 'form': form})


def ver_todos_los_mensajes(request):
    mensajes = Mensaje.objects.all().order_by('-fecha_creacion')

    paginator = Paginator(mensajes, 20)  
    page = request.GET.get('page', 1)

    try:
        mensajes_pagina = paginator.page(page)
    except PageNotAnInteger:
        mensajes_pagina = paginator.page(1)
    except EmptyPage:
        mensajes_pagina = paginator.page(paginator.num_pages)

    return render(request, 'mensajes/ver_todos_los_mensajes.html', {'mensajes_pagina': mensajes_pagina})

