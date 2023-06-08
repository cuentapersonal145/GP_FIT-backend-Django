# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class TipoProyecto(models.Model):
    """
    Clase usada para registrar los tipos de proyecto manegados en el contexto actual
    - - - - -
    Attributes
    - - - - -
    nombre : str(64)
        Nombre para identificar el tipo del proyecto
    date_record : datetime
        Fecha de registro
    date_update : datetime
        Fecha de último cambio realizado
    is_active : boolean
        Indica si el registro esta activo
    - - - - -
    Methods
    - - - - -
    """
    nombre = models.CharField(max_length=64, blank=True, unique=True)
    #tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    
    date_record = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Tipo Proyecto")
        verbose_name_plural = ("Tipos Proyectos")

    def __str__(self):
        return str(self.id) + " : " + self.nombre
