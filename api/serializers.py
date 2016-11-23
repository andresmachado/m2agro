from rest_framework import serializers
from .models import Product, Harvest, Service, ProductServiceRelationship


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'unit', 'price')


class ProductServiceRelationshipSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='product.id')
    name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = ProductServiceRelationship
        fields = ('id', 'name', 'quantity')


class ServiceSerializer(serializers.ModelSerializer):
    product = ProductServiceRelationshipSerializer(source='productservicerelationship_set', many=True)
    class Meta:
        model = Service
        fields = ('id', 'harvest', 'name', 'initial_date', 'end_date', 'total_cost', 'product')


class HarvestSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Harvest
        fields = ('id', 'name', 'initial_date', 'end_date', 'services')