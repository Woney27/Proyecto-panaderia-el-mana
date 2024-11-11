from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion_productos/', include('apps.gestion_productos.urls',)),
    path('gestion_insumos/', include('apps.gestion_insumos.urls')),
    path('gestion_ventas/', include('apps.gestion_ventas.urls')),
    path('gestion_empleados/', include('apps.gestion_empleados.urls')),
    path('usuarios/', include('apps.gestion_usuario.urls')),
    path('gestion_reporte/', include('apps.gestion_reporte.urls')),
    path('proveedores/', include('apps.gestion_proveedores.urls')),
    path('', TemplateView.as_view(template_name='base/PaginaPortada.html'), name='home'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
