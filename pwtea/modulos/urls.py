# urls.py
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .viewsets import ModuloViewSet

router = DefaultRouter()
router.register(r'modulo', ModuloViewSet)

urlpatterns = [
    path('modulos/', include(router.urls)),
    # Otras URL de tu aplicación (si las tienes)
]
