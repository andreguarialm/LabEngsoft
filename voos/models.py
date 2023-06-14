from django.db import models

# Create your models here.
class VooPiloto(models.Model):
    data = models.DateField()
    hora_chegada = models.DateTimeField()
    hora_saida = models.DateTimeField()

class VooAluno(models.Model):
    data = models.DateField()
    hora_chegada = models.DateTimeField()
    hora_saida = models.DateTimeField()
    parecer = models.CharField(max_length=200)