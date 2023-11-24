# urls.py
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import (ModuloViewSet, CategoriaViewSet, CategorizeListaViewSet, ActividadPictogramaListViewSet,
                    ActividadPictogramaViewSet, ActividadPictogramaActivoViewSet, CategorizeListaActivoViewSet,
                    ActividadOrdenarOracionViewSet, ActividadOrdenarOracionActivoViewSet,
                    ActividadOrdenarOracionListViewSet, PalabraViewSet)

router = DefaultRouter()
router.register(r'v1/modulos', ModuloViewSet)
router.register(r'v1/categorias', CategoriaViewSet)
router.register(r'v1/actividades_pictograma', ActividadPictogramaViewSet)
router.register(r'v1/actividades_ordenar_oracion', ActividadOrdenarOracionViewSet)
router.register(r'v1/palabras', PalabraViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('v1/modulos/<uuid:modulo_id>/modulo-categorias/', CategorizeListaViewSet.as_view()),
    path('v1/modulos/<uuid:modulo_id>/modulo-categorias/activas/', CategorizeListaActivoViewSet.as_view()),
    path('v1/actividades/pictograma/<uuid:categoria_id>/', ActividadPictogramaListViewSet.as_view()),
    path('v1/actividades/pictograma/activas/<uuid:categoria_id>/', ActividadPictogramaActivoViewSet.as_view()),
    path('v1/actividades/ordenar-oracion/<uuid:categoria_id>/', ActividadOrdenarOracionListViewSet.as_view()),
    path('v1/actividades/ordenar-oracion/activas/<uuid:categoria_id>/', ActividadOrdenarOracionActivoViewSet.as_view()),
]
