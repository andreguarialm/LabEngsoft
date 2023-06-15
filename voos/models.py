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
    socio = models.ForeignKey("usuarios.Socio", on_delete=models.CASCADE, related_name="voos")
    hora_chegada = models.DateTimeField()
    hora_saida = models.DateTimeField()
    
class AcompanhamentoVoo(models.Model):
    voo = models.OneToOneField("voos.Voo", on_delete=models.CASCADE)
    nota = models.FloatField()
    parecer = models.TextField(default="")
    instrutor = models.ForeignKey("usuarios.Socio", on_delete=models.CASCADE)
    
    