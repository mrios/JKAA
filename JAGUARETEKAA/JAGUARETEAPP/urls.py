from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name= "home"),
    path('buscador/', views.buscador, name="buscador" ),
    path('buscar/', views.buscar, name="buscar" ),
    path('detalle_producto/<int:id>', views.detalleProducto, name="detalle_producto" ),
    path('agregarproducto/', views.agregarProducto, name="agregarproducto" ),
   
    
]