from rest_framework import viewsets, generics, filters
from wishlist_app.models import Client, Product, Fav_Product
from wishlist_app.serializer import ClientSerializer, ProductSerializer, FavProductSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# class ApiViewSet(viewsets.ModelViewSet):
#     """API de Produtos Favoritos"""

class ClientsViewSet(viewsets.ModelViewSet):
    """Todos os clientes"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ProductsViewSet(viewsets.ModelViewSet):
    """Todos os produtos"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title']
    search_fields = ['title', 'brand']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class FavProductsViewSet(viewsets.ModelViewSet):
    """Listas de produtos favoritos de cada cliente"""
    queryset = Fav_Product.objects.all()
    serializer_class = FavProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['client__name']
    search_fields = ['client__name']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]