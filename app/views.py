# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, generics
#from rest_framework.response import Response
#from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse

from .models import *
from .serializers import *

# from django.db.models.signals import post_save
# from .signal import *

#--------------------------------------- Signals ----------------------------------------#

#post_save.connect(save_or_send_prod, sender=Producto)

#--------------------------------------- API´s por defecto ----------------------------------------#

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializador

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializador

class TipoProyectoViewSet(viewsets.ModelViewSet):
    queryset = TipoProyecto.objects.all()
    serializer_class = TipoProyectoSerializador

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializador
    
class DecisionViewSet(viewsets.ModelViewSet):
    queryset = Decision.objects.all()
    serializer_class = DecisionSerializador

class ActividadTipoViewSet(viewsets.ModelViewSet):
    queryset = ActividadTipo.objects.all()
    serializer_class = ActividadTipoSerializador
    
class ProyectoServicioViewSet(viewsets.ModelViewSet):
    queryset = ProyectoServicio.objects.all()
    serializer_class = ProyectoServicioSerializador

#--------------------------------------- API´s ----------------------------------------#

def RequerimientosProyectoAPI(request, id):
    query = f"""
                SELECT a.id, a.servicio_id, b.nombre as nombre_servicio, a.proyecto_id, c.nombre as nombre, a.tipo_proyecto_id, d.nombre as nombre_tipo, a.solicitud_id, e.nombre as nombre_solicitud
                FROM "main"."app_proyectoservicio" a 
                INNER JOIN "main"."app_servicio" b ON a.servicio_id = b.id
                INNER JOIN "main"."app_proyecto" c ON a.proyecto_id = c.id
                INNER JOIN "main"."app_tipoproyecto" d ON a.tipo_proyecto_id = d.id
                INNER JOIN "main"."app_solicitud" e ON a.solicitud_id = e.id
                WHERE a.servicio_id = {id} AND a.is_active = 1;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        
    data = []
    for row in results:
        item = {
            'id': row[0],
            'servicio_id': row[1],
            'nombre_servicio': row[2],
            'proyecto_id': row[3],
            'nombre': row[4],
            'tipo_proyecto_id': row[5],
            'nombre_tipo': row[6],
            'solicitud_id': row[7],
            'nombre_solicitud': row[8],
        }
        data.append(item)
    
    return JsonResponse(data, safe=False)

'''class DatosProductoAPI(generics.RetrieveAPIView):
    queryset = Producto.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Producto.objects.filter(marca_id=kwargs['id'])
        serializer = DatosProductoSerializador(queryset, many=True)
        return Response(serializer.data)'''
