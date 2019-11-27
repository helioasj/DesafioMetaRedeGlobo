from rest_framework import generics
from .models import Acmeplay
from .serializers import AcmeplaySerializer

# Create your views here.
class AcmeplayList(generics.ListCreateAPIView):

    queryset = Acmeplay.objects.all()
    serializer_class = AcmeplaySerializer

class AmceplayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Acmeplay.objects.all()
    serializer_class = AcmeplaySerializer
