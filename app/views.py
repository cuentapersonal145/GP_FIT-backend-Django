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

#--------------------------------------- API´s ----------------------------------------#

'''class DatosProductoAPI(generics.RetrieveAPIView):
    queryset = Producto.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Producto.objects.filter(marca_id=kwargs['id'])
        serializer = DatosProductoSerializador(queryset, many=True)
        return Response(serializer.data)'''
