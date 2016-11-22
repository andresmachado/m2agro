from rest_framework import serializers
from .models import Product, Harvest, Service


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'service', 'name', 'quantity', 'unit', 'price')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'harvest', 'name', 'initial_date', 'end_date', 'total_cost')


class HarvestSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Harvest
        fields = ('id', 'name', 'initial_date', 'end_date', 'services')