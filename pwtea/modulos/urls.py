# urls.py
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import ModuloViewSet, CategoriaViewSet, CategorizeListaViewSet

router = DefaultRouter()
router.register(r'v1/modulos', ModuloViewSet)
router.register(r'v1/categorias', CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('v1/modulos/<uuid:modulo_id>/modulo-categorias/', CategorizeListaViewSet.as_view()),
    # Otras URL de tu aplicación (si las tienes)
]
