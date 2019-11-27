from rest_framework import generics
from .models import Contato
from .serializers import ContatoSerializer

# Create your views here.
class ContatoList(generics.ListCreateAPIView):

    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class ContatoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer