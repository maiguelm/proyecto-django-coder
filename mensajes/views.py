from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mensajes.models import Mensaje



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

