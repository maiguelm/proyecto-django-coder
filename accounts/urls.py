from django.urls import path
from accounts.views import login, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
	path('login/', login, name='login'),
 	path("logout/", LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
  	path('login/register', register, name='register'),
]
