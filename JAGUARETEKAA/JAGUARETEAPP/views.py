
from django.shortcuts import redirect, render, get_object_or_404
from django.http.response import HttpResponse
from JAGUARETEAPP.models import Producto
from django.forms import modelform_factory
from JAGUARETEAPP.forms import ProductoForm
# Create your views here.


def home(request):
    productos=Producto.objects.all()
    return render(request, "web/home.html", {"productos": productos})

def buscador(request):
    return render(request, 'web/buscador.html')

def buscar(request):
    
    if request.GET["producto_buscado"]:
        producto=request.GET["producto_buscado"] 
        articulo=Producto.objects.filter(nombre__icontains=producto)
        return render(request, 'web/resultado_busqueda.html', {"articulo":articulo, "query":producto})
    else:
        mensaje= "No hay busquedas existentes"
    
    return HttpResponse(mensaje)


def detalleProducto(request, id):
    producto= get_object_or_404(Producto, pk=id)
    return render(request, "web/detalle_producto.html", {"producto":producto})


def agregarProducto(request):
    if request.method=="POST":
        producto_form = ProductoForm(request.POST, request.FILES, instance=Producto(imagen=request.FILES['imagen']))
        
        
        if producto_form.is_valid():
            producto_form.save()
            return redirect("home")
    else:
        producto_form = ProductoForm()
    return render(request, "web/agregar_producto.html", {"agregar_prod": producto_form })



def editar_producto(request, producto_id):
    producto_editado = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        
        
        form = ProductoForm(data=request.POST, files=request.FILES, instance=producto_editado)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProductoForm(instance = producto_editado)
        
        context = {
           
            "producto": producto_editado,
            "form": form
        }
        return render(request, 'web/producto_editado.html', context)

def producto_borrado(request, producto_id):
    borrado = get_object_or_404(Producto, id=producto_id)
    borrado.delete()
    return redirect("home")


