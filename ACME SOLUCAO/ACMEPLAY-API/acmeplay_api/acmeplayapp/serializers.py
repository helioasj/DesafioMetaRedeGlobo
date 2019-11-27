from rest_framework import serializers
from .models import Acmeplay

class AcmeplaySerializer(serializers.ModelSerializer):

    class Meta:

        model = Acmeplay
        fields = '__all__'
