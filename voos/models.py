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
    
    def __str__(self):
        return f"({self.socio}) {self.hora_saida} - {self.hora_chegada}"
    
class AcompanhamentoVoo(models.Model):
    voo = models.OneToOneField("voos.Voo", on_delete=models.CASCADE, related_name="acompanhamento")
    nota = models.FloatField()
    parecer = models.TextField(default="")
    instrutor = models.ForeignKey("usuarios.Socio", on_delete=models.CASCADE)

