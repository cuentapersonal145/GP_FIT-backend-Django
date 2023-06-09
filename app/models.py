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
    nombre = models.CharField(max_length=64, blank=False, null=False, unique=True)
    
    date_record = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Tipo Proyecto")
        verbose_name_plural = ("Tipos Proyectos")

    def __str__(self):
        return str(self.id) + " : " + self.nombre
    
class Proyecto(models.Model):
    """
    Clase usada para registrar los proyectos manegados en el contexto actual
    - - - - -
    Attributes
    - - - - -
    nombre : str(128)
        Nombre para identificar el proyecto
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
    nombre = models.CharField(max_length=128, blank=False, null=False, unique=True)
    
    date_record = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Proyecto")
        verbose_name_plural = ("Proyectos")

    def __str__(self):
        return str(self.id) + " : " + self.nombre

class Decision(models.Model):
    """
    Clase usada para registrar los proyectos manegados en el contexto actual
    - - - - -
    Attributes
    - - - - -
    tipo : int
        Campo adicional para identificar la decision
    descripcion : str(32)
        Valor de la desicion
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
    tipo = models.IntegerField(blank=False, null=False)
    descripcion = models.CharField(max_length=32, blank=False, null=False, unique=True)
    
    date_record = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Decision")
        verbose_name_plural = ("Decisiones")

    def __str__(self):
        return str(self.id) + " : " + str(self.tipo) + " : " + self.descripcion
    
class ActividadTipo(models.Model):
    """
    Clase usada para registrar las actividades por tipo de proyecto manegados en el contexto actual
    - - - - -
    Attributes
    - - - - -
    tipo_proyecto : FK
        Llave foranea en la relacion con el tipo de proyecto
    posicion : int
        Posicion de la actividad en el tipo de proyecto
    categoria : str(32)
        Categoria de la actividad
    decision : FK
        Llave foranea en la relacion con decision
    posicion_anterior : int
        Posicion anterior a la actual actividad en el tipo de proyecto
    nombre : str(256)
        Nombre para identificar la actividad
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
    tipo_proyecto = models.ForeignKey(TipoProyecto, blank=False, null=False, on_delete=models.CASCADE)
    posicion = models.PositiveIntegerField(blank=False, null=False)
    posicion_anterior = models.PositiveIntegerField(blank=True, null=True)
    categoria = models.CharField(max_length=32, blank=False, null=False)
    decision = models.ForeignKey(Decision, blank=True, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=64, blank=False, null=False)
    
    date_record = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Actividad por Tipo")
        verbose_name_plural = ("Actividades por Tipo")

    def __str__(self):
        main_desc = str(self.id) + " " + self.tipo_proyecto.nombre + " : Pos = " + str(self.posicion) 
        if self.posicion_anterior is not None:
            main_desc = main_desc + " --- Pos ant = " + str(self.posicion_anterior)
        main_desc = main_desc + " --- (" + self.nombre + ")"
        if self.decision is not None:
            main_desc = main_desc + " --- " + self.decision.descripcion
        return main_desc

class Requerimiento(models.Model):
    """
    Clase usada para registrar los requerimientos manegados en el contexto actual
    - - - - -
    Attributes
    - - - - -
    nombre : str(256)
        Nombre para identificar el requerimiento
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
    nombre = models.CharField(max_length=256, blank=False, null=False, unique=True)
    
    date_record = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Requerimiento")
        verbose_name_plural = ("Requerimientos")

    def __str__(self):
        return str(self.id) + " : " + self.nombre

class RequerimientoProyecto(models.Model):
    """
    Clase usada para registrar las actividades de cada proyecto
    - - - - -
    Attributes
    - - - - -
    proyecto : FK
        Llave foranea en la relacion con el proyecto
    tipo_proyecto : FK
        Llave foranea en la relacion con el tipo de proyecto
    requerimiento : FK
        Llave foranea en la relacion con el requerimiento
    actividades_tipo : FK
        Llave foranea en la relacion con el actividades por tipo de proyecto
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
    proyecto = models.ForeignKey(Proyecto, blank=False, null=False, on_delete=models.CASCADE)
    tipo_proyecto = models.ForeignKey(TipoProyecto, blank=False, null=False, on_delete=models.CASCADE)
    requerimiento = models.ForeignKey(Requerimiento, blank=False, null=False, on_delete=models.CASCADE)
    
    date_record = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Requerimiento por Proyecto")
        verbose_name_plural = ("Requerimientos por Proyectos")

    def __str__(self):
        main_desc = self.proyecto.nombre + " : " + self.tipo_proyecto.nombre + " : " + self.requerimiento.nombre
        if self.actividad_tipo.decision is not None:
            main_desc = main_desc + " => " + self.actividad_tipo.decision.descripcion
        return main_desc
    
    # def __str__(self):
    #     main_desc = self.proyecto.nombre + " : " + self.tipo_proyecto.nombre + " : " + self.requerimiento.nombre + " | (" + self.actividad_tipo.nombre + ")" 
    #     if self.actividad_tipo.decision is not None:
    #         main_desc = main_desc + " => " + self.actividad_tipo.decision.descripcion
    #     return main_desc
