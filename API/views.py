from django.shortcuts import render
from rest_framework import viewsets
from .serializer import prestamoSerializer, usuarioSerializer, libroSerializer, autorSerializer
from .models import Prestamo, Usuario, Libro, Autor

# Create your views here.

class prestamoSerializer(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = prestamoSerializer
    
class usuarioSerializer(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = usuarioSerializer
    
class libroSerializer(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = libroSerializer
    
class autorSerializer(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = autorSerializer
    
