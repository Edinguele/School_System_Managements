"""
URL configuration for school_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    # Interface d'administration Django
    path('admin/', admin.site.urls),

    # URLs de l'application "students"
    path('students/', include('students.urls')),

    # URLs de l'application "teachers"
    path('teachers/', include('teachers.urls')),

    # URLs de l'application "timetables"
    path('timetables/', include('timetables.urls')),

    # URLs de l'application "communication"
    path('communication/', include('communication.urls')),

    # URLs de l'application "finance"
    path('finance/', include('finance.urls')),

    # URLs de l'application "reporting"
    path('reporting/', include('reporting.urls')),

    # Page d'accueil (optionnelle)
    path('', include('home.urls')),  # Si vous avez une application "home" pour la page d'accueil
]
