from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from usuarios.models import Socio
from .models import Voo

# Create your views here.
def index(request):
    return HttpResponse("You are at voos index")

def voos(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)    
    return render(request, "voos-socio.html", {"voos": socio.voos.order_by("-hora_saida"), "socio": socio})
    