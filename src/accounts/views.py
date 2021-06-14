from django.contrib.auth import views as auth_views
from django.shortcuts import resolve_url

class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
