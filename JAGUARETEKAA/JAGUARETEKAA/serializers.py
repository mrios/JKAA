# serializers.py
from rest_framework import serializers

from JAGUARETEAPP.models import Producto

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion')

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"