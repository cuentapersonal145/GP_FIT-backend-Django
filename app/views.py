# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, generics
#from rest_framework.response import Response
#from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse

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
    
class RequerimientoViewSet(viewsets.ModelViewSet):
    queryset = Requerimiento.objects.all()
    serializer_class = RequerimientoSerializador
    
class RequerimientoProyectoViewSet(viewsets.ModelViewSet):
    queryset = RequerimientoProyecto.objects.all()
    serializer_class = RequerimientoProyectoSerializador

#--------------------------------------- API´s ----------------------------------------#

def RequerimientosProyectoAPI(request, id):
    query = f"""
                SELECT a.id, a.proyecto_id, b.nombre as nombre_proyecto, a.tipo_proyecto_id, c.nombre as nombre_tipo, a.requerimiento_id, d.nombre as nombre_requerimiento
                FROM "main"."app_actividadproyecto" a 
                INNER JOIN "main"."app_proyecto" b ON a.proyecto_id = b.id
                INNER JOIN "main"."app_tipoproyecto" c ON a.tipo_proyecto_id = c.id
                INNER JOIN "main"."app_requerimiento" d ON a.requerimiento_id = d.id
                WHERE a.proyecto_id = 1 AND a.is_active = 1
                GROUP BY a.id, a.proyecto_id, b.nombre, a.tipo_proyecto_id, c.nombre, a.requerimiento_id, d.nombre;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        
    data = []
    for row in results:
        item = {
            'id': row[0],
            'proyecto_id': row[1],
            'nombre_proyecto': row[2],
            'tipo_proyecto_id': row[3],
            'nombre_tipo': row[4],
            'requerimiento_id': row[5],
            'nombre': row[6],
        }
        data.append(item)
    
    return JsonResponse(data, safe=False)

'''class DatosProductoAPI(generics.RetrieveAPIView):
    queryset = Producto.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Producto.objects.filter(marca_id=kwargs['id'])
        serializer = DatosProductoSerializador(queryset, many=True)
        return Response(serializer.data)'''
