from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from proyectomoyano.views import DeletWine, DetailWine, UpdateWine, buscarVinos, inicio, about, contact, wines

urlpatterns = [
	path('', inicio, name='inicio'),
    path('about/', about, name='about'),
    path("busquedavinos/wines/", wines, name="wines"),
    path('busquedavinos/<int:pk>/', DetailWine.as_view(), name='detail_wine'),
    path('busquedavinos/<int:pk>/update/', UpdateWine.as_view(), name='update_wine'),
    path("busquedavinos/<int:pk>/eliminar", DeletWine.as_view(), name="delete_wines"),
    path("busquedavinos/", buscarVinos, name='busquedavinos'),
    path('contact/', contact, name='contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

