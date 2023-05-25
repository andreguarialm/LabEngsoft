from rest_framework.serializers import ModelSerializer, CharField
from .models import Socio

class SocioSerializer(ModelSerializer):
    class Meta:
        model = Socio
        fields = ["id", "nome", "breve"]