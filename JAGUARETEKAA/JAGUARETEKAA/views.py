# views.py
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from .serializers import ProductoSerializer
from JAGUARETEAPP.models import Producto

from rest_framework.views import APIView


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('nombre')
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class ProductoNike(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    renderer_classes = [JSONRenderer]

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, format=None):
        """
        Return a list of all users.from requerysetst_framework.views import APIView
        """
        
        productos_nike = Producto.objects.filter(Categoria=6)
        content = {'productos_nike': productos_nike}
        return Response(content)