from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeDoneView

from accounts.views import ChangePassword, login, register, editUser, Profile

urlpatterns = [
	path('login/', login, name='login'),
 	path("logout/", LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
  	path('login/register', register, name='register'),
    path('login/profile/<int:pk>/', Profile.as_view(), name='profile'),
   	path('login/profile/<int:pk>/edit_user/', editUser, name='edit_user'),
    path('login/profile/<int:pk>/edit_user/change_password', ChangePassword.as_view(), name='change_password'),
	path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
