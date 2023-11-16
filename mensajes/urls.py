from django.urls import path
from mensajes.views import ver_todos_los_mensajes 

app_name = 'mensajes'

urlpatterns = [
    path('ver-todos/', ver_todos_los_mensajes, name='ver_todos_los_mensajes')
]
