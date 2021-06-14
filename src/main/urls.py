"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path, re_path
from organization.views import TeamsView

from project.views import ProjectView
from search.views import SearchView

urlpatterns = [
    path('status/', include('health.urls')),
    re_path(r'^api/(?P<version>v[0-9]+)/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('', ProjectView.as_view(), name='root'),
    path(
        'login/', LoginView.as_view(template_name='accounts/login.html'), name='login'
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('projects/', ProjectView.as_view(), name='projects'),
    path('teams/', TeamsView.as_view(), name='teams'),
    path('search/', SearchView.as_view(), name='search'),
)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
