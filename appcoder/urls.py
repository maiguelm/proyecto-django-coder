from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('proyectomoyano.urls')),
    path('whiskies/', include('whiskies.urls')),
    path('accounts/', include('accounts.urls')),
    path('mensajes/', include('mensajes.urls', namespace='mensajes')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
