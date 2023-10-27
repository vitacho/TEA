# serializers.py
from rest_framework import serializers
from .models import Modulo, Categoria, Actividad, ActividadPictogramas, ActividadDibujo, ActividadMemoria, \
    ActividadComunicacion


class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = ['id', 'nombre', 'imagen', 'descripcion', 'tipo']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'imagen', 'descripcion', 'modulo', 'activo']


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['id', 'nombre', 'descripcion', 'tipo', 'activo', 'categoria']


class ActividadaPictogramasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadPictogramas
        fields = ['id', 'nombre', 'descripcion', 'tipo', 'activo', 'categoria', 'nombre_pictograma', 'descripcion_pictograma', 'imagen_pictograma', 'orden']

class ActividadFactory:
    @staticmethod
    def crear_actividad(tipo, *args, **kwargs):
        if tipo == 'dibujo':
            return ActividadDibujo(*args, **kwargs)
        elif tipo == 'pictogramas':
            return ActividadPictogramas(*args, **kwargs)
        elif tipo == 'memoria':
            return ActividadMemoria(*args, **kwargs)
        elif tipo == 'comunicacion':
            return ActividadComunicacion(*args, **kwargs)
        else:
            raise ValueError('Tipo de actividad no soportado')

class ActividadViewSet(serializers.ModelSerializer):
    def create(self, validated_data):
        tipo = validated_data.pop('tipo')
        actividad = ActividadFactory.crear_actividad(tipo, **validated_data)
        actividad.save()
        return actividad

