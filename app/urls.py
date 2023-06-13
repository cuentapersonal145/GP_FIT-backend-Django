from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
'''from django.conf import settings
from django.conf.urls.static import static'''

from .views import *
from . import views

router = DefaultRouter()

router.register('servicios', ServicioViewSet)
router.register('proyectos', ProyectoViewSet)
router.register('tipos_proyectos', TipoProyectoViewSet)
router.register('solicitudes', SolicitudViewSet)
router.register('decisiones', DecisionViewSet)
router.register('actividades_tipos', ActividadTipoViewSet)
router.register('proyectos_servicios', ProyectoServicioViewSet)

urlpatterns = [
    path( 'api/', include(router.urls) ),
    path( 'api/servicio/<int:id>/proyectos/', RequerimientosProyectoAPI ),
    # path( 'api/custom/', views.RequerimientosProyectoAPI, name='custom_api' ),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
