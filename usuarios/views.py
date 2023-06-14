
from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import Socio, Documento

# Create your views here.

def index(request):
    return HttpResponse("Usuarios.")
    return Socio.objects.all()
    return Documento.objects.all()
