from django.contrib import admin
from .models import  Categoria, Producto
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display=("nombre", "color", "precio")
    search_fields=("nombre", "color")

admin.site.register(Producto, ProductosAdmin)
admin.site.register(Categoria)


