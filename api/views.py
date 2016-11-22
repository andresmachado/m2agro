from django.shortcuts import render
from rest_framework import filters, generics, permissions, status, viewsets

from .serializers import ProductSerializer, HarvestSerializer, ServiceSerializer
from .models import Product, Harvest, Service

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    """Endpoint for add, delete and update products."""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ServiceViewSet(viewsets.ModelViewSet):
    """Endpoint for add, delete and update services."""
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class HarvestViewSet(viewsets.ModelViewSet):
    """Endpoint for add, delete and update harvests."""
    serializer_class = HarvestSerializer
    queryset = Harvest.objects.all()