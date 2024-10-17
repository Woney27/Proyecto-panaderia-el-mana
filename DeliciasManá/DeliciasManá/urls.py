from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion_productos/', include('apps.gestion_productos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
