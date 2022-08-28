"""login_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from loginapp import views
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register/', views.regis, name='register'),
    path('info', views.info),
    path("api/", api.urls),
    path("profile/", views.login_validate),
    path("profile/edit/", views.edit),
    path("profile/edit/submit/", views.submit)
]
