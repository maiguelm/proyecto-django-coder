from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as user_init
from django.views import View
from django.urls import reverse_lazy

from accounts.forms import UserRegister, UserEdit
from accounts.models import UserProfile


def login(request):
    
    if request.method == 'POST':
       formulario = AuthenticationForm(request, data=request.POST)
       if formulario.is_valid():
            user = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            user_registrer = authenticate(username=user, password=password)
            user_init(request, user_registrer)
            
            UserProfile.objects.get_or_create(user=request.user)
            
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

# class Profile(DetailView):
#     model = UserProfile()
#     template_name = "accounts/profile.html"
#     context_object_name = 'user_profile'
    
#     def get_object(self, queryset=None):
#         return UserProfile.objects.get(user=self.request.user)

class Profile(View):
    template_name = 'accounts/profile.html'

    def get(self, request, *args, **kwargs):
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        context = {'user_profile': user_profile}
        return render(request, self.template_name, context)

    
# def editUser(request, pk):
#     form = UserEdit(instance=request.user)
#     if request.method == 'POST':
#         form = UserRegister(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('edit_user')
    
#     return render(request, "accounts/edit_user.html", {'form': form})

def editUser(request, pk):
    user_extra = request.user.userprofile
    user = request.user
    form = UserEdit(initial={'lugar_residencia': user_extra.lugar_residencia, 'img_profile': user_extra.img_profile}, instance=request.user)

    if request.method == 'POST':
        form = UserEdit(request.POST, request.FILES, instance=user)

        if form.is_valid():
            lugar_residencia = form.cleaned_data.get('lugar_residencia')
            new_img_profile = form.cleaned_data.get('img_profile')
            
            if lugar_residencia:
                user_extra.lugar_residencia = lugar_residencia
            if new_img_profile:
                user_extra.img_profile = new_img_profile
            
            user_extra.save()
            form.save()
            return redirect('profile',pk=user.id)

    return render(request, "accounts/edit_user.html", {'form': form})

class ChangePassword(PasswordChangeView):
   template_name= 'accounts/change_password.html'
   success_url: reverse_lazy('password_change_done')