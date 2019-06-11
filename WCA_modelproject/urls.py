"""WCA_modelproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import WCA_modelapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WCA_modelapp.views.home, name='home'),
    path('about/', WCA_modelapp.views.about, name="about"),
    path('count/', WCA_modelapp.views.wordcount, name='wordcount'),
]
