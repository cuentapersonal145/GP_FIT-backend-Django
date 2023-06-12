from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
'''from django.conf import settings
from django.conf.urls.static import static'''

from .views import *

router = DefaultRouter()

router.register('tipo_proyecto', TipoProyectoViewSet)
router.register('proyecto', ProyectoViewSet)
router.register('decision', DecisionViewSet)
router.register('actividad_tipo', ActividadTipoViewSet)
router.register('requerimiento', RequerimientoViewSet)
router.register('actividad_proyecto', ActividadProyectoViewSet)

urlpatterns = [
    path( 'api/', include(router.urls) ),
    #path( 'api/productos/marca/<int:id>/', DatosProductoAPI.as_view() )
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
