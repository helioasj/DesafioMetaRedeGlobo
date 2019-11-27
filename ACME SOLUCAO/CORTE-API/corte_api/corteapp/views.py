from rest_framework import generics
from .models import Videos
from .serializers import VideosSerializer

# Create your views here.
class VideosList(generics.ListCreateAPIView):

    queryset = Videos.objects.all()
    serializer_class = VideosSerializer

class VideosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
