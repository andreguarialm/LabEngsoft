
from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import Socio
# Create your views here.

def index(request):
    return HttpResponse("Usuarios.")

def usuarios(request):
    objs = Socio.objects.all()
    return render(request, "lista-usuarios.html", {"objs": objs})

