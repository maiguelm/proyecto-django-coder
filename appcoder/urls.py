from django.contrib import admin
from django.urls import path, include
from proyectomoyano.views import inicio, about

urlpatterns = [
    path('', include('proyectomoyano.urls')),
    path('admin/', admin.site.urls)
]
