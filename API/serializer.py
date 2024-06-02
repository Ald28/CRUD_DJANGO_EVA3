from rest_framework import serializers
from .models import Usuario, Prestamo, Autor, Libro

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'nacionalidad']
        

class prestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'
    


class autorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class libroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
        