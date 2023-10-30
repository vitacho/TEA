import uuid
from django.db import models

PICTOGRAMA = 'PIC'
DIBUJO = 'DIB'
MEMORIA = 'MEM'

CHOICE_TIPO = [
  (PICTOGRAMA, 'Pictograma'),
  (DIBUJO, 'Dibujo'),
  (MEMORIA, 'Memoria'),
]

# Create your models here

class Modulo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(null=False, max_length=250)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='modulos_imagen/', null=False, blank=False)
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
    imagen = models.ImageField(upload_to='cateoria_imagen/', null=False, blank=False)
    creado = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True, null=False, blank=False)
    actualizado = models.DateTimeField(auto_now=True)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, null=False, blank=False)

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
        return self.nombre


class ActividadDibujo(Actividad):
    imagen = models.ImageField(upload_to='actividad_imagen/', null=True, blank=True)


class ActividadPictogramas(Actividad):
    #nombre_pictograma = models.CharField(null=False, max_length=250)
    #descripcion_pictograma = models.CharField(null=False, max_length=250)
    imagen_pictograma = models.ImageField(upload_to='actividad_imagen/', null=True, blank=True)
    orden = models.PositiveBigIntegerField(blank=True, null=True)
    # metodo para obtener el orden de la actividad pictograma
    def save(self, *args, **kwargs):
        if not self.orden:  # Si no se ha especificado un orden
            count = ActividadPictogramas.objects.filter(categoria=self.categoria).count()
            self.orden = count + 1  # Asignar el siguiente número en secuencia
        super(ActividadPictogramas, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.nombre} - {self.orden}"
    # metodo para obtener el orden de la actividad pictograma


class ActividadMemoria(Actividad):
    imagen = models.ImageField(upload_to='actividad_imagen/', null=True, blank=True)


class ActividadComunicacion(Actividad):
    dato = models.CharField(null=False, max_length=250)


class ActividadEscritura(Actividad):
    dato = models.CharField(null=False, max_length=250)


class ActividadGramaticaOrtografia(Actividad):
    dato = models.CharField(null=False, max_length=250)


class ActividadOrdenarPalabras(Actividad):
    palabras = models.CharField(null=False, max_length=250)


class ActividadPercepcion(Actividad):
    imagen = models.ImageField(upload_to='actividad_imagen/', null=True, blank=True)


class ActividadFiguraFondo(Actividad):
    imagen = models.ImageField(upload_to='actividad_imagen/', null=True, blank=True)


class ResulatadosActividad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ninio = models.ForeignKey(Ninio, on_delete=models.CASCADE, null=False, blank=False)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=False, blank=False)
    creado = models.DateTimeField(auto_now_add=True)
    tiempoenresolver = models.IntegerField(null=False)



