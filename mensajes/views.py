from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from mensajes.models import Mensaje



@login_required
def lista_mensajes(request):
    # Obtener todos los mensajes relacionados con el usuario autenticado
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
        contenido = request.POST.get('contenido')

        # Verificar que el contenido no esté vacío
        if contenido:
            Mensaje.objects.create(remitente=request.user, destinatario=destinatario, contenido=contenido)
            return redirect('ver_conversacion', destinatario_id=destinatario_id)
        else:
            return render(request, 'mensajes/enviar_mensaje.html', {'destinatario': destinatario, 'error': 'El mensaje no puede estar vacío'})

    return render(request, 'mensajes/enviar_mensaje.html', {'destinatario': destinatario})

@login_required
def ver_conversacion(request, destinatario_id):
    destinatario = get_object_or_404(User, id=destinatario_id)

    # Obtener la conversación entre el usuario autenticado y el destinatario
    conversacion = Mensaje.objects.filter(
        (Q(remitente=request.user) & Q(destinatario=destinatario)) |
        (Q(remitente=destinatario) & Q(destinatario=request.user))
    ).order_by('fecha_creacion')

    # Marcar los mensajes como leídos
    Mensaje.objects.filter(destinatario=request.user, remitente=destinatario, fecha_creacion__lte=conversacion.last().fecha_creacion).update(leido=True)

    return render(request, 'mensajes/ver_conversacion.html', {'conversacion': conversacion, 'destinatario': destinatario})

def ver_todos_los_mensajes(request):
    mensajes = Mensaje.objects.all().order_by('-fecha_creacion')

    paginator = Paginator(mensajes, 10)  # Mostrar 10 mensajes por página
    page = request.GET.get('page', 1)

    try:
        mensajes_pagina = paginator.page(page)
    except PageNotAnInteger:
        mensajes_pagina = paginator.page(1)
    except EmptyPage:
        mensajes_pagina = paginator.page(paginator.num_pages)

    return render(request, 'mensajes/ver_todos_los_mensajes.html', {'mensajes_pagina': mensajes_pagina})
