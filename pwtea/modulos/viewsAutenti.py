# api/views.py
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializersAutenti import RegistrationSerializer, UsuariosSerealizer

class RegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(request)
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuariosListAPIView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsuariosSerealizer
    permission_classes = [IsAuthenticated]

 #Inicio de session 
    
#Registro de usuarios
# Path: pwtea/modulos/viewsAutenti.py

class RegistroUsuario (generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        usuario= resquest.data['username']
        email= resquest.data['email']
        password= resquest.data['password']
        nombre= resquest.data['first_name']
        apellido= resquest.data['last_name']
        
        if not usuario:
            return Response({'Error': "Se requiere un nombre de usuario"}, status=status.HTTP_400_BAD_REQUEST)
        if not email:
            return Response({'Error': "Se requiere un email"}, status=status.HTTP_400_BAD_REQUEST)                  
        
        


        return self.create(request, *args, **kwargs)