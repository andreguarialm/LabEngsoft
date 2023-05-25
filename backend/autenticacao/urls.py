

from django.urls import path

from .views import SocioListCreateView


urlpatterns = [
    path("socios/", SocioListCreateView.as_view())
]