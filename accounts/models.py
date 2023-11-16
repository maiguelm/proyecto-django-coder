from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lugar_residencia = models.CharField(max_length=330, null=True)
    fecha_nacimiento=models.DateField(null=True)
    img_profile = models.ImageField(upload_to = 'imagenes', null=True, blank=True)
