
from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", include("login.urls"), name ='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='inicial/logout.html'), name='logout'),
    path("voos/", include("voos.urls"), name ='voos'), #add
    path("usuarios/", include("usuarios.urls"), name ='usuarios'), 
    path("", include("inicial.urls"), name ='inicial'), 
    path('admin/', admin.site.urls, name ='admin'),
    #path('accounts/', include("django.contrib.auth.urls"), name ='accounts'),

]
