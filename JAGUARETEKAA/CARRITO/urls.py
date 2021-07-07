from django.urls import path
from . import views

app_name="CARRITO"

urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto, name= "agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name= "eliminar"),
    path("quitar/<int:producto_id>/", views.quitar_producto, name= "quitar"),
    path("limpiar/<int:producto_id>/", views.limpiar_carrito, name= "limpiar"),

]