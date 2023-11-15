from django.urls import path
from mensajes.views import lista_mensajes, enviar_mensaje, ver_conversacion, ver_todos_los_mensajes

app_name = 'mensajes'

urlpatterns = [
    path('mensajes/', lista_mensajes, name='lista_mensajes'),
    path('enviar/<str:destinatario_username>/', enviar_mensaje, name='enviar_mensaje'),
    path('conversacion/<int:destinatario_id>/', ver_conversacion, name='ver_conversacion'),
    path('ver-todos/', ver_todos_los_mensajes, name='ver_todos_los_mensajes')
]
