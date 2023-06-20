from django.contrib import admin
from .models import Voo, AcompanhamentoVoo
from .forms import VooForm, AcompanhamentoVooForm

@admin.register(Voo)
class VooAdmin(admin.ModelAdmin):
    form = VooForm
    list_display = ("socio", "hora_saida", "hora_chegada", "acompanhado", "instrutor")
    
    def acompanhado(self, obj):
        return obj.acompanhamento is not None
    
    def instrutor(self, obj):
        return obj.acompanhamento.instrutor

@admin.register(AcompanhamentoVoo)
class AcompanhamentoVooAdmin(admin.ModelAdmin):
    form = AcompanhamentoVooForm
    list_display = ("voo", "nota", "parecer", "instrutor")
    
    

