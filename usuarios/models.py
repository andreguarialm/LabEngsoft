import datetime
from django.db import models
from django.utils import timezone
# from django.contrib.auth impor
from django.conf import settings
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
        return self.certificado_instrutor is not None
    
    @property
    def is_piloto(self):
        return self.breve != ""
    
    @property
    def is_aluno(self):
        return self.breve == ""
    

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