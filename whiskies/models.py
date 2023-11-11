from django.db import models


class Whisky(models.Model):
    TIPOS = (
        ('whisky', 'Whisky'),
        ('bourbon', 'Bourbon'),
        ('otros', 'Otros')
    )
    etiqueta = models.CharField(max_length=30)
    aniejamiento = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=120)
    tipo = models.CharField(max_length=30, choices=TIPOS,default='whisky')
    fecha_compra = models.DateField(null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f'{self.id} - {self.etiqueta} - {self.descripcion} - {self.aniejamiento}'
