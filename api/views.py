from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializer import *



class DatosViewSet(viewsets.ModelViewSet):
    queryset = Datos.objects.all()
    serializer_class = DatosSerializer
