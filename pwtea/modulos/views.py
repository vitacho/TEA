from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import Modulo, Categoria, Actividad, ActividadPictogramas, ActividadOrdenarOracion, Palabra
from .serializers import (ModuloSerializer, CategoriaSerializer, ActividadaPictogramasSerializer,
                          ActividadOrdenarOracionSerializer, PalabraSerializer)
from django.shortcuts import get_object_or_404

from django.db import transaction
import re
import nltk
# from nltk.world_tokenize import word_tokenize


class ModuloViewSet(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer


"""
views de Categorias
"""


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    # manejo de peticion post para la creacion de categorias
    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()  # Crea una copia mutable del QueryDict
        if 'activo' not in mutable_data:
            # Establece activo en True si no se recibe ningún valor
            mutable_data['activo'] = True

        serializer = CategoriaSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # manejo de peticiones path y put
    def update(self, request, *args, **kwargs):

        print("Entra a update")
        categoria = self.get_object()
        actividades_relacionadas = Actividad.objects.filter(
            categoria=categoria)
        print(actividades_relacionadas)

        if 'activo' in request.data and not request.data['activo'] and actividades_relacionadas.exists():
            return Response({"message": "No se puede desactivar la categoría ya que existen "
                                        "actividades relacionadas"},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(
                categoria, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            print(serializer.data)
            return Response(serializer.data)


class CategorizeListaViewSet(generics.ListAPIView):
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        modulo_id = self.kwargs.get('modulo_id')
        modulo = get_object_or_404(Modulo, id=modulo_id)

        categorias = Categoria.objects.filter(modulo=modulo)

        # Verifica si existen categorías relacionadas con el módulo
        if not categorias.exists():
            # Si no existen categorías, puedes devolver una respuesta personalizada, como un mensaje de error
            
            return []

        return categorias


class CategorizeListaActivoViewSet(generics.ListAPIView):
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        modulo_id = self.kwargs.get('modulo_id')
        modulo = get_object_or_404(Modulo, id=modulo_id)

        categorias = Categoria.objects.filter(modulo=modulo, activo=True)

        # Verifica si existen categorías relacionadas con el módulo
        if not categorias.exists():
            # Si no existen categorías, puedes devolver una respuesta personalizada, como un mensaje de error

            return []

        return categorias


"""
views de actividades pictogramas
"""


class ActividadPictogramaViewSet(viewsets.ModelViewSet):
    queryset = ActividadPictogramas.objects.all()
    serializer_class = ActividadaPictogramasSerializer

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()  # Crea una copia mutable del QueryDict

        if 'activo' not in mutable_data:
            # Establece activo en True si no se recibe ningún valor
            mutable_data['activo'] = True

        if 'tipo' not in mutable_data:
            mutable_data['tipo'] = 'PIC'

        if 'descripcion' not in mutable_data:
            mutable_data['descripcion'] = ' '

        serializer = ActividadaPictogramasSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # Agregar control cuando se tenga reportes listos


class ActividadPictogramaListViewSet(generics.ListAPIView):
    serializer_class = ActividadaPictogramasSerializer

    def get_queryset(self):
        # Obtenemos la categoria correpdiente
        categoria_id = self.kwargs.get('categoria_id')

        # Filtar las actividades de pictogramas que pertenecen a la categoria solo las activas
        categoria = get_object_or_404(Categoria, id=categoria_id)

        #
        actividades = ActividadPictogramas.objects.filter(
            categoria=categoria).order_by('orden')
        if not actividades.exists():
            return []
        return actividades


class ActividadPictogramaActivoViewSet(generics.ListAPIView):
    serializer_class = ActividadaPictogramasSerializer

    def get_queryset(self):
        # Se obtienen la categorias correspondiente
        categoria_id = self.kwargs.get('categoria_id')
        # Se obtienen las actividades de pictogramas que pertenecen a la categoria solo las activas
        categoria = get_object_or_404(Categoria, id=categoria_id)
        # Se filtran las actividades de pictogramas que pertenecen a la categoria solo las activas
        actividades = ActividadPictogramas.objects.filter(
            activo=True, categoria=categoria)
        actividades = actividades.filter(activo=True)
        print(actividades[1].activo)
        # Se verifica si existen actividades de pictogramas que pertenecen a la categoria solo las activas
        if not actividades.exists():
            '''
            Si no existen actividades de pictogramas que pertenecen a la categoria solo las activas,
            se deuelve un lista vacia

            '''
            return []
        return actividades


'''
Actividades de Ordenamiento de palabras con imagenes
'''


class ActividadOrdenarOracionViewSet(viewsets.ModelViewSet):
    queryset = ActividadOrdenarOracion.objects.all()
    serializer_class = ActividadOrdenarOracionSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        serializer = ActividadOrdenarOracionSerializer(data=mutable_data)
        if 'tipo' not in mutable_data:
            mutable_data['tipo'] = 'ORD'

        if serializer.is_valid():
            instance = serializer.save()
            if 'oracion' in mutable_data:
                # nltk.download('punkt') # se debe descargar la libreria punkt antes de usarla por primera vez
                oracion = mutable_data['oracion']
                # volvemos miniúscula la oración para no crear palabras cuando tenga alguna letra en mayusculas y elminamos los espacios en blanco
                oracion = oracion.lower()
                oracion = re.sub(r'\s+', ' ', oracion)
                # separamos la oracion en palabras
                oracion_token = nltk.word_tokenize(oracion, 'spanish')
                print(oracion_token)
                palabras_creadas = []
                for palabra in oracion_token:

                    # se verifica si la palabra ya existe en la base de datos
                    if Palabra.objects.filter(texto=palabra.lower()).exists():
                        # si existe se agrega a la lista de plabras
                        obj = Palabra.objects.get(texto=palabra.lower())
                        instance.palabras.add(obj)
                    else:
                        # Se crea la palabra si no exite
                        obj, create = Palabra.objects.get_or_create(
                            texto=palabra.lower())
                        if create:
                            palabras_creadas.append(obj.id)
                        instance.palabras.add(obj)
                for id in palabras_creadas:
                    instance.palabras.add(id)

            return Response({
                'actividad': serializer.data,
                'palabras_creadas': palabras_creadas
            }, status=201)
        else:
            return Response(serializer.errors, status=400)

    def update(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        instance = self.get_object()
        serializer = ActividadOrdenarOracionSerializer(instance, data=mutable_data)
        if 'tipo' not in mutable_data:
            mutable_data['tipo'] = 'ORD'

        if serializer.is_valid():
            instance = serializer.save()
            if 'oracion' in mutable_data:
                oracion = mutable_data['oracion'].lower()
                oracion = re.sub(r'\s+', ' ', oracion)
                oracion_token = nltk.word_tokenize(oracion, 'spanish')

                palabras_creadas = []
                for palabra in oracion_token:
                    if Palabra.objects.filter(texto=palabra.lower()).exists():
                        obj = Palabra.objects.get(texto=palabra.lower())
                        instance.palabras.add(obj)
                    else:
                        obj, created = Palabra.objects.get_or_create(texto=palabra.lower())
                        if created:
                            palabras_creadas.append(obj.id)
                        instance.palabras.add(obj)

                # Get current words and remove those not in the new list
                current_words = instance.palabras.all()
                for word in current_words:
                    if word.texto not in oracion_token:
                        instance.palabras.remove(word)

            return Response({
                'actividad': serializer.data,
                'palabras_creadas': palabras_creadas
            }, status=200)
        else:
            return Response(serializer.errors, status=400)


class ActividadOrdenarOracionListViewSet(generics.ListAPIView):
    serializer_class = ActividadOrdenarOracionSerializer

    def get_queryset(self):
        # Obtenemos la categoria correspondiente
        categoria_id = self.kwargs.get('categoria_id')

        # Filtrar las actividades de pictogramas que pertenecen a la categoria solo las activas
        categoria = get_object_or_404(Categoria, id=categoria_id)

        #
        actividades = ActividadOrdenarOracion.objects.filter(
            categoria=categoria)
        if not actividades.exists():
            return []
        return actividades


class ActividadOrdenarOracionActivoViewSet(generics.ListAPIView):

    serializer_class = ActividadOrdenarOracionSerializer

    def get_queryset(self):
        # Se obtienen la categorias correspondiente
        categoria_id = self.kwargs.get('categoria_id')
        # Se obtienen las actividades de pictogramas que pertenecen a la categoria solo las activas
        categoria = get_object_or_404(Categoria, id=categoria_id)
        # Se filtran las actividades de pictogramas que pertenecen a la categoria solo las activas
        actividades = ActividadOrdenarOracion.objects.filter(
            categoria=categoria, activo=True)
        # Se verifica si existen actividades de pictogramas que pertenecen a la categoria solo las activas
        if not actividades.exists():
            '''
            Si no existen actividades de pictogramas que pertenecen a la categoria solo las activas,
            se devuelve un lista vacía

            '''
            return []
        return actividades


class PalabraViewSet(viewsets.ModelViewSet):
    queryset = Palabra.objects.all()
    serializer_class = PalabraSerializer

    # manejo de peticion post para la creacion de palabras
    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        serializer = PalabraSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
