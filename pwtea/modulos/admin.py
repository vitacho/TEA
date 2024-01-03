from django.contrib import admin
from .models import Modulo, Categoria, Actividad, ActividadPictogramas, ActividadOrdenarOracion,Palabra
from rest_framework.authtoken.admin import TokenAdmin
admin.site.register(Modulo)
admin.site.register(Categoria)
admin.site.register(Actividad)
admin.site.register(ActividadPictogramas)
admin.site.register(ActividadOrdenarOracion)
admin.site.register(Palabra)


# Register your models here.



TokenAdmin.raw_id_fields = ['user']