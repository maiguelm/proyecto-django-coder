from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from whiskies.views import CreateWhisky, DeleteWhisky, DetailWhisky, UpdateWhisky, Whiskies


urlpatterns = [
    path("find_whisky/", Whiskies.as_view(), name="find_whisky"),    
    path("find_whisky/whiskies/", CreateWhisky.as_view(), name="whiskies"),
    path("find_whisky/<int:pk>/update", UpdateWhisky.as_view(), name="update_whiskies"),
    path("find_whisky/<int:pk>/detail", DetailWhisky.as_view(), name="detail_whiskies"),
    path("find_whisky/<int:pk>/delete", DeleteWhisky.as_view(), name="delete_whiskies"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)