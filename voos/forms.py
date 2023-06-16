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
        fields = ["voo", "nota", "parecer"]

    #instrutor = self.user.socio
    