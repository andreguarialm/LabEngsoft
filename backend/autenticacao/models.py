from mailbox import NotEmptyError
from sqlite3 import Cursor
from django.db import models
from .querysets import SocioQuerySet

# Create your models here.
    
class Socio(models.Model):
    nome = models.CharField(max_length=100)
    breve = models.CharField(max_length=5, default=None, null=True, unique=True)
    doc = models.OneToOneField(DocumentoInstrutor, on_delete=models.CASCADE, default = None, null = True)
    
    objects = SocioQuerySet.as_manager()
    
    def __str__(self) -> str:
        return self.nome
    
    @property
    def is_aluno(self):
        return self.breve is None
    
    @property
    def is_piloto(self):
        return self.breve is not None
    
    @property
    def is_instrutor(self):
        return self.doc is not None

class DocumentoInstrutor(models.Model):
    curso = models.CharField(max_length=30)
    instituicao = models.CharField(max_length=50)
    data = models.DateField()

class Funcionario(models.Model)
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=100)
    idade = models.ImageField()