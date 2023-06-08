from rest_framework import serializers

from .models import *

#--------------------------------------- Serializadores por defecto ----------------------------------------#

class TipoProyectoSerializador(serializers.ModelSerializer):
    #tipo = PrincipalesDatosTipo(read_only=True)
    class Meta:
        model = TipoProyecto
        fields = '__all__'

#-------------------------------------------------------------------------------#

class PrincipalesDatosTipoProyecto(serializers.ModelSerializer):
    class Meta:
        model = TipoProyecto
        fields = ('id', 'nombre')
