from django.db import models
from datetime import datetime, timedelta
from django.db.models.functions import Extract
from django.template.defaultfilters import slugify
from django.core.exceptions import PermissionDenied
  
# class Voo(models.Model):
#     socio = models.ForeignKey("usuarios.Socio", on_delete=models.CASCADE, related_name="voos")
#     hora_chegada = models.DateTimeField()
#     hora_saida = models.DateTimeField()
    
#     def __str__(self):
#        return f"({self.socio}) {self.hora_saida} - {self.hora_chegada}"


#     @property
#     def duracao(self):
#         return (self.hora_chegada - self.hora_saida) #.total_seconds()/3600
    

#     def save(self, *args, **kwargs):
#         if not self.socio.classe == 'aluno' and not self.acompanhamento:
#             raise PermissionDenied("Voos de alunos requerem um AcompanhamentoVoo.")
#         super().save(*args, **kwargs)

    
# class AcompanhamentoVoo(models.Model):
#     voo = models.OneToOneField("voos.Voo", on_delete=models.CASCADE, related_name="acompanhamento")
#     nota = models.FloatField()
#     parecer = models.TextField(default="")
#     instrutor = models.ForeignKey("usuarios.Socio", on_delete=models.CASCADE)

#############################

class Voo(models.Model):
    socio = models.ForeignKey("usuarios.Socio", on_delete=models.CASCADE, related_name="voos")
    hora_chegada = models.DateTimeField()
    hora_saida = models.DateTimeField()

    nota = models.PositiveSmallIntegerField(null= True, blank= True)
    parecer = models.TextField(default="", blank= True)
    instrutor = models.ForeignKey("usuarios.Socio", on_delete=models.CASCADE, null= True, blank=True)
    
    def __str__(self):
       return f"({self.socio}) {self.hora_saida} - {self.hora_chegada}"


    @property
    def duracao(self):
        return (self.hora_chegada - self.hora_saida) #.total_seconds()/3600
    

    def save(self, *args, **kwargs):
        if self.socio.classe == 'aluno' and (self.instrutor is None or self.nota is None ):
            raise PermissionDenied("Voos de alunos requerem um instrutor e uma nota.")
        super().save(*args, **kwargs)
