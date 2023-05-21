"""marianportal URL Configuration

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
from django.urls import path
from sites.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/', landing, name="Learn"),
    path('', main_html , name = "home"),
    path('profile/attendance/', attendance, name="attendance"),
    path('profile/',home, name="Home"),
    path('profile/requests/', requests, name="requests"),
    path('logout/', logout_view, name="logout"),
    path('enroll/', enroll, name="Enroll"),
    path('sendmodule/', sendmodule, name='formsend'),
    path('success/', success, name='Success'),
    path('subjects/<int:subject_id>/', subject_detail, name='subject_detail'),
    path('test', sendmodule, name='test')
]
