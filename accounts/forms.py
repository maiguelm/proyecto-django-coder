from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from mensajes.models import Mensaje

class UserRegister(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='Ingrese su nombre', widget=forms.TextInput(attrs={'placeholder': 'Ingresesu nombre'}))
    username = forms.CharField(max_length=30, label='Ingrese su nombre de usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        
class UserEdit(UserChangeForm):
    password:  None
    email = forms.EmailField(label="Cambiar correo electrónico", required=False, widget=forms.EmailInput(attrs={'type': 'email'}))
    first_name = forms.CharField(required=False, max_length=30, label='Cambiar su nombre', widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    last_name = forms.CharField(required=False, max_length=30, label='Cambiar su apellido', widget=forms.TextInput(attrs={'placeholder': 'Ingrese su apellido'}))
    fecha_nacimiento=forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    lugar_residencia = forms.CharField(label='Lugar de residencia', max_length=100, required=False)
    img_profile = forms.ImageField(label='Imagen de Usuario', required=False)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "lugar_residencia", "img_profile", "fecha_nacimiento"]

    def __init__(self, *args, **kwargs):
        super(UserEdit, self).__init__(*args, **kwargs)
        self.fields.pop('password')
        
class MensajeForm(forms.Form):
    destinatario = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)
    contenido = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí'}))
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'contenido']