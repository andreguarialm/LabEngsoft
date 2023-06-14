from django.db import models

# Create your models here.
class VooPiloto(models.Model):
    data = models.DateField()
    hora_chegada = models.TimeField()
    hora_saida = models.TimeField()

class VooAluno(models.Model):
    data = models.DateField()
    hora_chegada = models.TimeField()
    hora_saida = models.TimeField()
    parecer = models.CharField(max_length=200)