import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as user_init
from accounts.forms import UserRegister


def login(request):
    
    if request.method == 'POST':
       formulario = AuthenticationForm(request, data=request.POST)
       if formulario.is_valid():
            user = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            user_registrer = authenticate(username=user, password=password)
            user_init(request, user_registrer)
            
            return redirect('inicio')
       else:
           return render(request, 'accounts/login.html', {'formulario': formulario})
    
    formulario = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'formulario': formulario})

def register(request):
    formulario = UserRegister()
    
    if request.method == 'POST':
        formulario = UserRegister(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    
    
    return render(request, 'accounts/register.html', {'form':formulario})