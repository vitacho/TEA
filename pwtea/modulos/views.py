from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import Modulo, Categoria, Actividad, ActividadPictogramas
from .serializers import ModuloSerializer, CategoriaSerializer, ActividadaPictogramasSerializer
from django.shortcuts import get_object_or_404
import uuid

class ModuloViewSet(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    # manejo de peticion post para la creacion de categorias
    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()  # Crea una copia mutable del QueryDict
        if 'activo' not in mutable_data:
            mutable_data['activo'] = True  # Establece activo en True si no se recibe ningún valor

        serializer = CategoriaSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # manejo de peticiones path y put
    def update(self, request, *args, **kwargs):

        print("Entra a update")
        categoria = self.get_object()
        actividades_relacionadas = Actividad.objects.filter(categoria=categoria)
        print(actividades_relacionadas)

        if 'activo' in request.data and not request.data['activo'] and actividades_relacionadas.exists():
            return Response({"message": "No se puede desactivar la categoría ya que existen actividades relacionadas"},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(categoria, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            print(serializer.data)
            return Response(serializer.data)




class CategorizeListaViewSet(generics.ListAPIView):
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        modulo_id = self.kwargs.get('modulo_id')
        modulo = get_object_or_404(Modulo, id=modulo_id)

        categorias = Categoria.objects.filter(modulo=modulo, activo=True)

        # Verifica si existen categorías relacionadas con el módulo
        if not categorias.exists():
            # Si no existen categorías, puedes devolver una respuesta personalizada, como un mensaje de error}

            return []

        return categorias


class ActividadPictogramaViewSet(viewsets.ModelViewSet):
    queryset = ActividadPictogramas.objects.all()
    serializer_class = ActividadaPictogramasSerializer
    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()  # Crea una copia mutable del QueryDict
        if 'activo' not in mutable_data:
            mutable_data['activo'] = True  # Establece activo en True si no se recibe ningún valor

        serializer = CategoriaSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    #agregar control cuan hayan reporte ya listo:


class ActividadPictogramaListViewSet(generics.ListAPIView):
    serializer_class = ActividadaPictogramasSerializer
    def get_queryset(self):

            #Obtenemos la categoria correpdiente
            categoria_id = self.kwargs.get('categoria_id')

            #Filtar las actividades de pictogramas que pertenecen a la categoria solo las activas
            categoria = get_object_or_404(Categoria, id=categoria_id)

            #
            actividades = ActividadPictogramas.objects.filter(categoria=categoria).order_by('orden')
            if not actividades.exists():
                return []
            return actividades
