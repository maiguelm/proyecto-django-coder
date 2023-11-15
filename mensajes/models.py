# mensajes/models.py
from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    contenido = models.TextField()
    remitente = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.remitente.username} -> {self.destinatario.username}: {self.contenido}'
