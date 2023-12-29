# serializers.py
from rest_framework import serializers
from .models import Modulo, Categoria, Actividad, ActividadPictogramas, ActividadDibujo, ActividadMemoria, \
    ActividadComunicacion, ActividadOrdenarOracion, Palabra


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
        fields = ['id', 'nombre', 'descripcion', 'tipo', 'activo', 'categoria', 'imagen_pictograma', 'orden']


'''
Activiades de Ordenamiento de palabras con imagenes
'''


class ActividadOrdenarOracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadOrdenarOracion
        fields = ['id', 'nombre', 'descripcion', 'tipo', 'activo', 'categoria', 'oracion',
                  'palabras']

    def get_frases(self, obj):
        return obj.obtener_frases()


'''
Frases de las actividades de ordenar oracion
'''


class PalabraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palabra
        fields = ['id', 'texto', 'imagen']
