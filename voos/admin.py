from django.contrib import admin
from .models import Voo 
from .forms import VooForm

@admin.register(Voo)
class VooAdmin(admin.ModelAdmin):
    form = VooForm
    list_display = ("socio", "hora_saida", "hora_chegada", "instrutor", "nota", "parecer")
    
    def acompanhado(self, obj):
        return (obj.instrutor and obj.nota) is not None
    
    def instrutor(self, obj):
        return obj.instrutor

# @admin.register(AcompanhamentoVoo)
# class AcompanhamentoVooAdmin(admin.ModelAdmin):
#     form = AcompanhamentoVooForm
#     list_display = ("voo", "nota", "parecer", "instrutor")
    
    

