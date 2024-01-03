import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


PICTOGRAMA = 'PIC'
DIBUJO = 'DIB'
MEMORIA = 'MEM'
ORDENAR_ORACION = 'ORD'

CHOICE_TIPO = [
    (PICTOGRAMA, 'Pictograma'),
    (DIBUJO, 'Dibujo'),
    (MEMORIA, 'Memoria'),
    (ORDENAR_ORACION, 'Ordenar Oración'),
]


# agregar campos al modelo de usuario

# Create your models here

class Modulo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(null=False, max_length=250)
    descripcion = models.TextField()
    imagen = models.ImageField(
        upload_to='modulos_imagen/', null=False, blank=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    tipo = models.CharField(choices=CHOICE_TIPO)


def __str__(self):
    return self.nombre


class Ninio(models.Model):
    MAS = 'M'
    FEM = 'F'
    GRADO_1 = 'G1'
    GRADO_2 = 'G2'
    GRADO_3 = 'G3'

    CHOICE_SEXO = ((MAS, 'Masculino'),
                   (FEM, 'Femenino'))

    CHOICE_GRADO_TEA = ((GRADO_1, 'Grado 1'),
                        (GRADO_2, 'Grado 2'),
                        (GRADO_3, 'Grado 3'))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(null=False, max_length=250)
    apellido = models.CharField(null=False, max_length=250)
    # edad=models.IntegerField(null=False)
    fecha_nacimiento = models.DateField(null=False)
    sexo = models.CharField(max_length=12, choices=CHOICE_SEXO)
    grado_tea = models.CharField(max_length=25, choices=CHOICE_GRADO_TEA)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(null=False, max_length=250, blank=False)
    descripcion = models.TextField()
    imagen = models.ImageField(
        upload_to='cateoria_imagen/', null=False, blank=False)
    creado = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True, null=False, blank=False)
    actualizado = models.DateTimeField(auto_now=True)
    modulo = models.ForeignKey(
        Modulo, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(null=False, max_length=250)
    descripcion = models.TextField(null=True, blank=True)
    tipo = models.CharField(choices=CHOICE_TIPO)
    activo = models.BooleanField(default=True, null=False, blank=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.id}"

    class Meta:
       # verbose_name = "Actividades"
        verbose_name_plural = "Actividades"

class ActividadDibujo(Actividad):
    imagen = models.ImageField(
        upload_to='actividad_imagen/', null=True, blank=True)


class ActividadPictogramas(Actividad):
    # nombre_pictograma = models.CharField(null=False, max_length=250)
    # descripcion_pictograma = models.CharField(null=False, max_length=250)
    imagen_pictograma = models.ImageField(
        upload_to='actividad_imagen/', null=True, blank=True)
    orden = models.PositiveBigIntegerField(blank=True, null=True)

    # metodo para obtener el orden de la actividad pictograma
    def save(self, *args, **kwargs):
        if not self.orden:  # Si no se ha especificado un orden
            count = ActividadPictogramas.objects.filter(
                categoria=self.categoria).count()
            self.orden = count + 1  # Asignar el siguiente número en secuencia
        super(ActividadPictogramas, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} - {self.orden}"
    # metodo para obtener el orden de la actividad pictograma


    class Meta:
        #verbose_name = "Actividad Pictogramas"
        verbose_name_plural = "Actividades Pictogramas"

class ActividadMemoria(Actividad):
    imagen = models.ImageField(
        upload_to='actividad_imagen/', null=True, blank=True)


class ActividadComunicacion(Actividad):
    dato = models.CharField(null=False, max_length=250)


class ActividadEscritura(Actividad):
    dato = models.CharField(null=False, max_length=250)


class ActividadGramaticaOrtografia(Actividad):
    dato = models.CharField(null=False, max_length=250)


class ActividadOrdenarOracion(Actividad):
    palabras = models.ManyToManyField('Palabra', blank=True)
    # frases_ordenadas = models.ManyToManyField('Palabra', blank=True, null=False, related_name='frases_ordenadas')
    # imagen_ordenar = models.ImageField(upload_to='actividad_imagen/', null=True, blank=True)
    # Cambair a false despues
    oracion = models.CharField(null=True, max_length=250, blank=True)

    class Meta:
        #verbose_name = "Actividad Ordenar Oraciones"
        verbose_name_plural = "Actividades Ordenar Oraciones"


class Palabra(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    texto = models.CharField(null=False, max_length=250,
                             blank=False, unique=True)
    imagen = models.ImageField(
        upload_to='frases_imagen/', null=True, blank=True)

    def __str__(self):
        return self.texto


# Clases de frases many to many Actividadoracion

class ActividadPercepcion(Actividad):
    imagen = models.ImageField(
        upload_to='actividad_imagen/', null=True, blank=True)


class ActividadFiguraFondo(Actividad):
    imagen = models.ImageField(
        upload_to='actividad_imagen/', null=True, blank=True)


class ResulatadosActividad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ninio = models.ForeignKey(
        Ninio, on_delete=models.CASCADE, null=False, blank=False)
    actividad = models.ForeignKey(
        Actividad, on_delete=models.CASCADE, null=False, blank=False)
    creado = models.DateTimeField(auto_now_add=True)
    tiempoenresolver = models.IntegerField(null=False)

    class Meta:
        #verbose_name = "Resultado de Actividad"
        verbose_name_plural = "Resultados de Actividades"


class Persona(models.Model):

    TIPO_ADMINISTRADOR = 'A'
    TIPO_PADRES = 'p'
    TIPO_ESPECIAISTA = 'E'
    TIPO_DOCENTE = 'D'

    CHOICE_TIPO = ((TIPO_ADMINISTRADOR, 'Administrador'),
                   (TIPO_PADRES, 'Padres'),
                   (TIPO_ESPECIAISTA, 'Especialista'),
                   (TIPO_DOCENTE, 'Docente'))


    email = models.EmailField(unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   # usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    ninio = models.ForeignKey(
        Ninio, on_delete=models.CASCADE, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    tipo_cuenta = models.CharField(
        max_length=1, choices=CHOICE_TIPO, default=TIPO_PADRES)
    activo = models.BooleanField(default=True, null=False, blank=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        #verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"