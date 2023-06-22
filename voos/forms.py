from django import forms
from .models import Voo

class VooForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ["socio", "hora_saida", "hora_chegada", "parecer", "nota", "instrutor"]

    def clean(self):
        data = super().clean()
        if data["hora_saida"] > data["hora_chegada"]:
            raise forms.ValidationError("Hora de saida precisa ser antes da hora de chegada")
        # if data["socio"].is_aluno:
        #     if data["instrutor"] is None:
        #         raise forms.ValidationError("Escolha o nome do instrutor deste voo no campo apropriado")
        #     if data["nota"] is None or data["nota"] > 10:
        #         raise forms.ValidationError("A nota deve estar entre 0 e 10")
        #     return data
    
# class AcompanhamentoVooForm(forms.ModelForm):
#     class Meta:
#         model = AcompanhamentoVoo
#         fields = ["voo", "nota", "parecer", "instrutor"]
    
#     def clean(self):
#         data = super().clean()
#         if not data["instrutor"].is_instrutor :
#             raise forms.ValidationError("Apenas instrutores podem acompanhar voos")
#         if data["nota"] > 10 or data["nota"] < 0:
#             raise forms.ValidationError("A nota deve estar entre 0 e 10")
#         return data

    #instrutor = self.user.socio
    