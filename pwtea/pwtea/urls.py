
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('modulos.urls')),
    path('docs/', include_docs_urls(title='API PWTEA')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Rutas para archivos multimedia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
