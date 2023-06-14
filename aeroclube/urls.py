
from django.contrib import admin
from django.urls import path, include #add

urlpatterns = [
    path("login/", include("login.urls")),
    path("polls/", include("polls.urls")), #add
    path("voos/", include("voos.urls")), #add
    path('admin/', admin.site.urls),

]
