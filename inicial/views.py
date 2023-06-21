from django.shortcuts import render, get_object_or_404
from usuarios.models import Socio
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.

#@login_required
def home(request):    
    if request.user.is_authenticated:
        if Socio.objects.filter(user = request.user).exists():
            socio = request.user.socio
            voos = socio.voos.order_by("-hora_saida")
            if Socio.classe == "aluno":
                horas = socio.horas_de_voo_aluno
                pode_tirar_breve = socio.pode_tirar_breve
            else:
                horas = {}
                pode_tirar_breve = {}
            ctx =  {
                "autenticado": True,
                "voos": [(len(voos) - i, voo) for i, voo in enumerate(voos)], 
                "socio": socio,
                #"duracao": socio.voos.hora_saida - socio.voos.hora_chegada 
                "duracao": socio.voos,
                "horas": horas
            }    
        else:
            ctx={"autenticado": True}
    else:
        ctx={}
    return render(request, 'inicial/home.html', ctx)
