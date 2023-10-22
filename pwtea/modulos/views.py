from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import Modulo, Categoria, Actividad
from .serializers import ModuloSerializer, CategoriaSerializer
from django.shortcuts import get_object_or_404


class ModuloViewSet(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    #manejo de peticion post para la creacion de categorias
    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()  # Crea una copia mutable del QueryDict
        if 'activo' not in mutable_data:
            mutable_data['activo'] = True  # Establece activo en True si no se recibe ningún valor

        serializer = CategoriaSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    #manejo de peticiones path y put
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



class CategoriaListaViewSet(generics.ListAPIView):
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
