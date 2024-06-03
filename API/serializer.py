# serializers.py
from rest_framework import serializers
from .models import Prestamo, Usuario, Libro, Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'nacionalidad']

class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    
    class Meta:
        model = Libro
        fields = ['id', 'codigo', 'titulo', 'isbn', 'editorial', 'num_pags', 'autor']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'num_usuario', 'nif', 'nombre', 'direccion', 'telefono']

class PrestamoSerializer(serializers.ModelSerializer):
    libro = LibroSerializer(read_only=True)
    usuario = UsuarioSerializer(read_only=True)
    
    class Meta:
        model = Prestamo
        fields = ['id', 'libro', 'usuario', 'fecha_prestamo', 'fecha_devolucion']
