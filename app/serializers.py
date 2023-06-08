from rest_framework import serializers

from .models import *

#--------------------------------------- Serializadores por defecto ----------------------------------------#

class TipoProyectoSerializador(serializers.ModelSerializer):
    #tipo = PrincipalesDatosTipo(read_only=True)
    class Meta:
        model = TipoProyecto
        fields = '__all__'
        
class ProyectoSerializador(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'
        
class DecisionSerializador(serializers.ModelSerializer):
    class Meta:
        model = Decision
        fields = '__all__'
        
class ActividadTipoSerializador(serializers.ModelSerializer):
    class Meta:
        model = ActividadTipo
        fields = '__all__'

class ProyectoTipoActividadSerializador(serializers.ModelSerializer):
    class Meta:
        model = ProyectoTipoActividad
        fields = '__all__'
        
#-------------------------------------------------------------------------------#

'''class PrincipalesDatosTipoProyecto(serializers.ModelSerializer):
    class Meta:
        model = TipoProyecto
        fields = ('id', 'nombre')'''
