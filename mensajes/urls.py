from django.urls import path
from mensajes.views import ver_todos_los_mensajes, lista_mensajes, enviar_mensaje

app_name = 'mensajes'

urlpatterns = [
    path('lista_mensajes/', lista_mensajes, name='lista_mensajes'),
    path('enviar/<str:destinatario_username>/', enviar_mensaje, name='enviar_mensaje'),
    path('ver-todos/', ver_todos_los_mensajes, name='ver_todos_los_mensajes')
]
