# urls.py
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .viewsets import ModuloViewSet

router = DefaultRouter()
router.register(r'modulos', ModuloViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Otras URL de tu aplicación (si las tienes)
]
