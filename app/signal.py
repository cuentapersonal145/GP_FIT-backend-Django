from django.db.models.signals import post_save
from .models import *

'''def save_or_send_prod(sender, instance, created, **kwargs):
    if instance.tipo.nombre == "Libra":
        newTipo = Tipo.objects.filter(nombre="Kilo")
        newProducto = Producto(marca=instance.marca, tipo=newTipo[0], categoria=instance.categoria, precio=instance.precio*2)
        newProducto.save()
    elif instance.tipo.nombre == "Media-Libra":
        newTipo = Tipo.objects.filter(nombre="Libra")
        newProducto = Producto(marca=instance.marca, tipo=newTipo[0], categoria=instance.categoria, precio=instance.precio*2)
        newProducto.save()'''
    