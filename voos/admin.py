from django.contrib import admin
from .models import Voo
from .forms import VooForm

@admin.register(Voo)
class VooAdmin(admin.ModelAdmin):
    form = VooForm
    list_display = ("socio", "hora_saida", "hora_chegada", "acompanhado")
    
    def acompanhado(self, obj):
        return obj.acompanhamento is not None
    

