from django.contrib import admin
from .models import  Categoria, Producto
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display=("nombre", "precio")
    search_fields=("nombre", "categoria")

admin.site.register(Producto, ProductosAdmin)
admin.site.register(Categoria)


