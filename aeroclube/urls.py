
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path("login/", include("login.urls")),
    path("voos/", include("voos.urls")), #add
    path("usuarios/", include("usuarios.urls")), 
    path('admin/', admin.site.urls),

]
