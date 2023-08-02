from django.db import models

# Create your models here

class Modulo(models.Model):

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(null=False,max_length=250)
    descripcion = models.TextField()
    #imagen =  models.ImageField(upload_to='modulos_imagen')
    creado = models.DateTimeField(auto_now_add=True)
    ## implemantar slug
def __str__(self):
    return self.nombre

