
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path("login/", include("login.urls"), name ='login'),
    path("voos/", include("voos.urls"), name ='voos'), #add
    path("usuarios/", include("usuarios.urls"), name ='usuarios'), 
    path("", include("inicial.urls"), name ='inicial'), 
    path('admin/', admin.site.urls, name ='admin'),
    #path('accounts/', include("django.contrib.auth.urls"), name ='accounts'),

]
