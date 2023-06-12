from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
'''from django.conf import settings
from django.conf.urls.static import static'''

from .views import *
from . import views

router = DefaultRouter()

router.register('tipo_proyecto', TipoProyectoViewSet)
router.register('proyectos', ProyectoViewSet)
router.register('decision', DecisionViewSet)
router.register('actividad_tipo', ActividadTipoViewSet)
router.register('requerimiento', RequerimientoViewSet)
router.register('requerimiento_proyecto', RequerimientoProyectoViewSet)

urlpatterns = [
    path( 'api/', include(router.urls) ),
    path( 'api/proyecto/<int:id>/requerimientos/', RequerimientosProyectoAPI ),
    # path( 'api/custom/', views.RequerimientosProyectoAPI, name='custom_api' ),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
