from django.db import models
from datetime import datetime, timedelta
from django.db.models.functions import Extract
from django.template.defaultfilters import slugify


# Create your models here.
# class VooPiloto(models.Model):
#     data = models.DateField()
#     hora_chegada = models.TimeField()
#     hora_saida = models.TimeField()

# class VooAluno(models.Model):
#     data = models.DateField()
#     hora_chegada = models.TimeField()
#     hora_saida = models.TimeField()
#     parecer = models.CharField(max_length=200)
    

class Voo(models.Model):
    socio = models.ForeignKey("usuarios.Socio", on_delete=models.CASCADE, related_name="voos")
    hora_chegada = models.DateTimeField()
    hora_saida = models.DateTimeField()
    #duracao = hora_saida.strftime('%Y') - hora_chegada.strftime('%Y')
    #duracao = (Extract(hora_chegada, "hour") - Extract(hora_saida, "hour"))
    
    def __str__(self):
       return f"({self.socio}) {self.hora_saida} - {self.hora_chegada}"
    #def __str__(self):
    #   return f"{self.duracao.strftime('%Y')}"

    @property
    def duracao(self):
        #return self.certificado_instrutor is not None
        return (self.hora_chegada - self.hora_saida) #.total_seconds()/3600
    
class AcompanhamentoVoo(models.Model):
    voo = models.OneToOneField("voos.Voo", on_delete=models.CASCADE, related_name="acompanhamento")
    nota = models.FloatField()
    parecer = models.TextField(default="")
    instrutor = models.ForeignKey("usuarios.Socio", on_delete=models.CASCADE)

