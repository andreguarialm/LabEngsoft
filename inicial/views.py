from django.shortcuts import render, get_object_or_404
from usuarios.models import Socio
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.

#@login_required
def home(request):    
    if Socio.objects.filter(user = request.user).exists():
        socio = request.user.socio
        voos = socio.voos.order_by("-hora_saida")
        ctx =  {
            "voos": [(len(voos) - i, voo) for i, voo in enumerate(voos)], 
            "socio": socio,
            #"duracao": socio.voos.hora_saida - socio.voos.hora_chegada 
            "duracao": socio.voos
        }    
    else:
        ctx={}
    return render(request, 'inicial/home.html', ctx)
