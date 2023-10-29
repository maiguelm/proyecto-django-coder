from django.db import models

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
    descripcion = models.CharField(max_length=120)
    tipo = models.CharField(max_length=30, choices=TIPOS,default='vino_tinto')
    
    def __str__(self):
        return f'{self.id} - {self.etiqueta} - {self.descripcion} - {self.cosecha}'

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
    
    def __str__(self):
        return f'{self.id} - {self.etiqueta} - {self.descripcion} - {self.aniejamiento}'

