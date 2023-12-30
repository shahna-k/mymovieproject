"""onlinemovie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from movie import views




app_name="movie"

urlpatterns = [

    path('',views.viewmovie,name="viewmovie"),
    path('addmovie/',views.addmovie,name="addmovie"),
    path('view/<int:p>/',views.viewbyid,name="viewbyid"),
    path('editbyid/<int:p>/',views.editbyid,name="editbyid"),
    path('deletebyid/<int:p>/',views.deletebyid,name="deletebyid"),

]


