from rest_framework import serializers
from .models import Videos

class VideosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Videos
        fields = ('id', 'nome','path','start_time', 'end_time','duration', 'status')
