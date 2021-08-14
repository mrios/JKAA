# views.py
from typing import Generic
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import serializers

from .serializers import ProductoSerializer
from JAGUARETEAPP.models import Producto, Categoria

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('nombre')
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductoNike(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Producto.objects.filter(categoria_id=6)
    serializer_class = ProductoSerializer

    def retrieve(self, request, *args, **kwargs):
        # ret = super(StoryViewSet, self).retrieve(request)
        # return Response({'key': 'single value', 'datos': self.queryset})
        return Response({'key': 'single value', 'datos': 'datos a serializar'})

    def list(self, request, *args, **kwargs):
        # ret = super(StoryViewSet, self).list(request)
        print(self.get_queryset())
        return Response({'key': 'single value', 'datos': 'datos a serializar'})