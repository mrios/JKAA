from django.shortcuts import render, redirect
from JAGUARETEAPP.models import Producto
from CARRITO.carrito import Carrito

# Create your views here.

def agregar_producto(request, producto_id):

    carrito= Carrito(request)
    producto= Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):

    carrito= Carrito(request)
    producto= Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def quitar_producto(request, producto_id):

    carrito= Carrito(request)
    producto= Producto.objects.get(id=producto_id)
    carrito.quitar(producto)
    return redirect("carrito")

def limpiar_carrito(request, producto_id):

    carrito= Carrito(request)
    carrito.elimina_carrito()
    return redirect("carrito")
