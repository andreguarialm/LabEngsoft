from django.db import models

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
    socio = models.OneToOneField("usuarios.Socio", on_delete=models.CASCADE)
    data = models.DateField()
    hora_chegada = models.TimeField()
    hora_saida = models.TimeField()
    
class AcompanhamentoVoo(models.Model):
    voo = models.OneToOneField("voos.Voo", on_delete=models.CASCADE)
    nota = models.FloatField()
    parecer = models.TextField()
    instrutor = models.ForeignKey("usuarios.Socio", on_delete=models.CASCADE)
    
    