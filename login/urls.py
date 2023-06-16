from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    #path("", views.login, name="login"),
    path("", auth_views.LoginView.as_view(template_name='inicial/login.html'), name='login'),
]