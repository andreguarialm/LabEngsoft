from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from usuarios.models import Socio
from .models import Voo

# Create your views here.
def index(request):
    return HttpResponse("You are at voos index")

def voos(request, socio_id):
    socio = get_object_or_404(Socio.objects.prefetch_related("voos__acompanhamento"), id=socio_id)
    voos = socio.voos.order_by("-hora_saida")
    ctx =  {
        "voos": [(len(voos) - i, voo) for i, voo in enumerate(voos)], 
        "socio": socio
    }    
    return render(request, "voos-socio.html", ctx)

