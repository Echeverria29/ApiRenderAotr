from .models import *
from rest_framework import serializers


class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos
        # fields = ('fullname', 'nickname')
        fields = '__all__'