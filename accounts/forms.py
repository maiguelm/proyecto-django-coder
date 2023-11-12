from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegister(UserCreationForm):
    name = forms.CharField(max_length=30, label='Ingrese su nombre', widget=forms.TextInput(attrs={'placeholder': 'Ingresesu nombre'}))
    username = forms.CharField(max_length=30, label='Ingrese su nombre de usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email'}))
    
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password1', 'password2']