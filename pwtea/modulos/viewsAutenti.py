import json
# api/views.py
from django.contrib.auth import get_user_model, authenticate

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny 
from .serializersAutenti import UsuariosSerealizer, RegistroUsuarioSerealizer, InicioSesionSerializer
from rest_framework.authentication import TokenAuthentication

from rest_framework.authtoken.models import Token


class UsuariosListAPIView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsuariosSerealizer
    permission_classes = [IsAuthenticated]

 # Inicio de session

# Registro de usuarios
# Path: pwtea/modulos/viewsAutenti.py


class RegistroUsuario (generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistroUsuarioSerealizer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)

            return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InicioSesion(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = InicioSesionSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        print(username)
        # Intenta autenticar por nombre de usuario
        user = authenticate(
            request, username=username, password=password)

        # Si la autenticación por nombre de usuario falla, intenta por correo electrónico
        if user is None:
            try:
                print("entro")
                print(username)

                user_obj = get_user_model().objects.get(email=username)
                print(user_obj)
                user = authenticate(
                    request, username=user_obj.username, password=password)
            except get_user_model().DoesNotExist:
                #imprimimos el error en la consola
                print("Error")
                pass

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            
            return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST)
'''
Verificamos el token del usario
'''
class ObtenerUsuario(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = get_user_model().objects.get(id=request.user.id)
        return Response({
            "username": user.username,
            "email": user.email,
            # Agrega aquí cualquier otro campo que quieras devolver.
        })