from django import forms
from .models import Voo, AcompanhamentoVoo

class VooForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ["socio", "hora_saida", "hora_chegada"]

    def clean(self):
        data = super().clean()
        if data["hora_saida"] > data["hora_chegada"]:
            raise forms.ValidationError("Hora de saida precisa ser antes da hora de chegada")
        return data
    
class AcompanhamentoVooForm(forms.ModelForm):
    class Meta:
        model = AcompanhamentoVoo
        fields = ["voo", "nota", "parecer", "instrutor"]
    
    def clean(self):
        data = super().clean()
        if not data["instrutor"].is_instrutor :
            raise forms.ValidationError("Apenas instrutores podem acompanhar voos")
        if data["nota"] > 10 or data["nota"] < 0:
            raise forms.ValidationError("A nota deve estar entre 0 e 10")
        return data

    #instrutor = self.user.socio
    