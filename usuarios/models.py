import datetime
from django.db import models
from django.utils import timezone
from datetime import timedelta
# from django.contrib.auth impor
from django.conf import settings
from voos.models import Voo 
from voos import models as voos_models
from django.db.models import Sum
# Create your models here.

class Socio(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="socio")
    idade = models.IntegerField()
    endereço = models.CharField(max_length=400)
    breve = models.CharField(max_length=20, default="", blank=True)  

    def __str__(self):
        return self.user.get_full_name()
    
    
    @property
    def is_instrutor(self):
        #return self.certificado_instrutor is not None
        return CertificadoIntrutor.objects.filter(socio=self).exists()
    
    @property
    def is_piloto(self):
        return self.breve != ""
    
    @property
    def is_aluno(self):
        return self.breve == ""
    
    @property
    def classe(self):
        if self.is_aluno:
            return "aluno"
        elif self.is_instrutor:
            return "instrutor"
        elif self.is_piloto:
            return "piloto"
        else:
            return ""
        

    
    @property
    def horas_de_voo_aluno(self):
        horas = datetime.timedelta(seconds=0)
        #print ("nota = " + str(v.acompanhamento.nota)) # o print faz o dado nao aparecer no html (why?????)
        for v in self.voos.all():
            if v.nota != None:
                if v.nota >= 5:
                    horas += v.duracao  
                #print(v.duracao)
            #print(v.acompanhamento.nota >= 4)
        #print(horas)
        return horas
    
    @property
    def pode_tirar_breve(self):
        #print(self.horas_de_voo_aluno)
        h = self.horas_de_voo_aluno
        if  h > timedelta(1) and self.breve == "":
            return True
        else:
            return False
    
    #@property
    #def pode_tirar_breve(self):
    #    return self.is_aluno and
    
    

class CertificadoIntrutor(models.Model):
    socio = models.OneToOneField(Socio, on_delete=models.CASCADE, primary_key=True, related_name="certificado_instrutor", limit_choices_to=~models.Q(breve=""))
    nome_curso = models.TextField(max_length=200, null=True, default="", blank=True)
    data_diploma = models.DateTimeField("Graduado em:", null=True, default=None, blank=True)

# class Documento(models.Model):
#     socio = models.OneToOneField(Socio, on_delete=models.CASCADE, primary_key=True)
#     #Piloto e Instrutor
#     breve = models.CharField(max_length=20, null=True, default="", blank=True)
#     #Instrutor
#     nome_curso = models.TextField(max_length=200, null=True, default="", blank=True)
#     data_diploma = models.DateTimeField("Graduado em:", null=True, default=None, blank=True)
#     #Aluno
#     data_matricula = models.DateTimeField("Matriculado em:", null=True, default=None, blank=True)
#     notas = models.FloatField(default=0)