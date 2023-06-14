from django.db import models

# Create your models here.

class Socio(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)
    endereço = models.CharField(max_length=400)

class Documentos(models.Model):
    #Piloto e Instrutor
    breve = models.CharField(max_length=20, null=True, default="")
    #Instrutor
    nome_curso = models.TextField(max_length=200, null=True, default="")
    data_diploma = models.DateTimeField("Graduado em:", null=True, default=None)
    #Aluno
    data_matricula = models.DateTimeField("Matriculado em:", null=True, default=None)
    notas = models.FloatField(default=0)