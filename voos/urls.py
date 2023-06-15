from django.urls import path

from .views import voos

urlpatterns = [
    path('<int:socio_id>/', voos, name='voos-do-usuario'),
]