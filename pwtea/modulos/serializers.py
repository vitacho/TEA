# serializers.py
from rest_framework import serializers
from .models import Modulo, Categoria

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = ['id', 'nombre','imagen', 'descripcion']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre','imagen', 'descripcion','modulo','activo']