from rest_framework.generics import ListCreateAPIView

from .models import Socio
from .serializers import SocioSerializer



class SocioListCreateView(ListCreateAPIView):
    serializer_class = SocioSerializer
    queryset = Socio.objects.all()


    

