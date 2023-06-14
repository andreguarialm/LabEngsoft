import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Socio(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)
    endereço = models.CharField(max_length=400)

    def __int__(self):
        return self.pk

class Documento(models.Model):
    socio = models.OneToOneField(Socio, on_delete=models.CASCADE, primary_key=True)
    #Piloto e Instrutor
    breve = models.CharField(max_length=20, null=True, default="")
    #Instrutor
    nome_curso = models.TextField(max_length=200, null=True, default="")
    data_diploma = models.DateTimeField("Graduado em:", null=True, default=None)
    #Aluno
    data_matricula = models.DateTimeField("Matriculado em:", null=True, default=None)
    notas = models.FloatField(default=0)