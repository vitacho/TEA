import uuid
from django.db import models

# Create your models here

class Modulo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(null=False,max_length=250)
    descripcion = models.TextField()
    imagen =  models.ImageField(upload_to='modulos_imagen/')
    creado = models.DateTimeField(auto_now_add=True)
    ## implemantar slug
def __str__(self):
    return self.nombre
class Nino(models.Model):
    MAS= 'M'
    FEM= 'F'
    GRADO_1='G1'
    GRADO_2='G2'
    GRADO_3='G3'

    CHOICE_SEXO = ((MAS, 'Masculino'),
                    (FEM, 'Femenino'))

    CHOICE_GRADO_TEA = ((GRADO_1,'Grado 1'),
                        (GRADO_2,'Grado 2'),
                        (GRADO_3,'Grado 3'))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre=models.CharField(null=False,max_length=250)
    apellido=models.CharField(null=False,max_length=250)
    #edad=models.IntegerField(null=False)
    fecha_nacimiento=models.DateField(null=False)
    sexo=models.CharField(max_length=12,choices=CHOICE_SEXO)
    grado_tea=models.CharField(max_length=25,choices=CHOICE_GRADO_TEA)
    creado = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre
class Actividad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre=models.CharField(null=False,max_length=250)
    descripcion=models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre