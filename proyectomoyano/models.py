from django.db import models
from ckeditor.fields import RichTextField

class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
    telefono = models.IntegerField()
    consulta = models.CharField(max_length=150)

class Vino(models.Model):
    TIPOS = (
        ('vino_tinto', 'Vino Tinto'),
        ('vino_blanco', 'Vino Blanco'),
        ('vino_rosado', 'Vino Rosado')
    )
    etiqueta = models.CharField(max_length=30)
    varietal = models.CharField(max_length=30)
    cosecha = models.IntegerField()
    descripcion = RichTextField()
    tipo = models.CharField(max_length=30, choices=TIPOS,default='vino_tinto')
    fecha_compra = models.DateField(null=True)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    
    def __str__(self):
        return f'{self.id} - {self.etiqueta} - {self.descripcion} - {self.cosecha}'

