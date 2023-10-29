from django.urls import path
from proyectomoyano.views import buscarVinos, inicio, about, contact, wines, whiskies

urlpatterns = [
	path('', inicio, name='inicio'),
    path('about/', about, name='about'),
    path("busquedavinos/wines/", wines, name="wines"),
    path("busquedavinos/", buscarVinos, name='busquedavinos'),
    path("whiskies/", whiskies, name="whiskies"),
    path('contact/', contact, name='contact')
]

