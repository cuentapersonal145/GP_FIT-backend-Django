from rest_framework import serializers

from .models import *

#--------------------------------------- Serializadores por defecto ----------------------------------------#

class ServicioSerializador(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class ProyectoSerializador(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class TipoProyectoSerializador(serializers.ModelSerializer):
    class Meta:
        model = TipoProyecto
        fields = '__all__'
        
class SolicitudSerializador(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'
        
class DecisionSerializador(serializers.ModelSerializer):
    class Meta:
        model = Decision
        fields = '__all__'
        
class ActividadTipoSerializador(serializers.ModelSerializer):
    class Meta:
        model = ActividadTipo
        fields = '__all__'

class ProyectoServicioSerializador(serializers.ModelSerializer):
    class Meta:
        model = ProyectoServicio
        fields = '__all__'
        
class ProyectoActividadSerializador(serializers.ModelSerializer):
    class Meta:
        model = ProyectoActividad
        fields = '__all__'
        
#-------------------------------------------------------------------------------#

# class PrincipalesDatosActividadProyecto(serializers.ModelSerializer):
#     # proyecto = PrincipalesDatosProyecto(read_only=True)
#     # tipo_proyecto = PrincipalesDatosTipoProyecto(read_only=True)
#     # requerimiento = PrincipalesDatosRequerimiento(read_only=True)
#     # actividad_tipo = PrincipalesDatosActividadTipo(read_only=True)
    
#     class Meta:
#         model = TipoProyecto
#         fields = ('id', 'proyecto', 'tipo_proyecto', 'requerimiento', 'actividad_tipo')
