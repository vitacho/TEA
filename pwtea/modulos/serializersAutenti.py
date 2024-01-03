# api/serializers.py

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import EmailValidator
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class UsuariosSerealizer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'date_joined',
                  'last_login', 'is_active', 'is_staff')


class RegistroUsuarioSerealizer(serializers.ModelSerializer):
    email = serializers.EmailField(
        write_only=True,
        validators=[

            EmailValidator(
                message="Por favor, introduce un correo electrónico válido."),
            UniqueValidator(queryset=get_user_model().objects.all(), message="El correo electrónico ya está en uso.")])

    password = serializers.CharField(
        write_only=True,
        validators=[validate_password],
        help_text='Requerido. Su contraseña no puede asemejarse tanto a su otra información personal. \n Su contraseña debe contener al menos 8 caracteres. \nSu contraseña no puede ser una clave utilizada comúnmente. \nSu contraseña no puede ser completamente numérica.'
    )
    password2 = serializers.CharField(
        write_only=True, required=True, help_text='Repetir contraseña')
    first_name = serializers.CharField(
        write_only=True,
        required=True, help_text='Requerido. Nombre del Usuario solo letras')
    last_name = serializers.CharField(
        write_only=True,
        required=True, help_text='Requerido. Apellido del Usuario solo letras')
    # email = serializers.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password',
                  'password2', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Las constraseñas no coinciden"})

        return attrs

    def validate_email(self, email):

        email = get_adapter().clean_email(email)
        return email

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class InicioSesionSerializer(serializers.Serializer):
    username = serializers.CharField(
        style={'placeholder': 'Usuario o Correo electrónico'}
    )
    password = serializers.CharField(
         style={'input_type': 'password', 'placeholder': 'Contraseña'}
    )
