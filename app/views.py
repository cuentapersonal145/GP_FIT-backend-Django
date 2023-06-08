# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, generics
#from rest_framework.response import Response
#from django.shortcuts import render

from .models import *
from .serializers import *

'''from django.db.models.signals import post_save
from .signal import *'''

#--------------------------------------- Signals ----------------------------------------#

#post_save.connect(save_or_send_prod, sender=Producto)

#--------------------------------------- API´s por defecto ----------------------------------------#

class TipoProyectoViewSet(viewsets.ModelViewSet):
    queryset = TipoProyecto.objects.all()
    serializer_class = TipoProyectoSerializador
    
class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializador
    
class DecisionViewSet(viewsets.ModelViewSet):
    queryset = Decision.objects.all()
    serializer_class = DecisionSerializador

class ActividadTipoViewSet(viewsets.ModelViewSet):
    queryset = ActividadTipo.objects.all()
    serializer_class = ActividadTipoSerializador
    
class ProyectoTipoActividadViewSet(viewsets.ModelViewSet):
    queryset = ProyectoTipoActividad.objects.all()
    serializer_class = ProyectoTipoActividadSerializador

#--------------------------------------- API´s ----------------------------------------#

'''class DatosProductoAPI(generics.RetrieveAPIView):
    queryset = Producto.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Producto.objects.filter(marca_id=kwargs['id'])
        serializer = DatosProductoSerializador(queryset, many=True)
        return Response(serializer.data)'''
