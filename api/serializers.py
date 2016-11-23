from rest_framework import serializers
from .models import Product, Harvest, Service, ProductServiceRelationship


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'unit', 'price')


class ProductServiceRelationshipSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source='product.name')

    class Meta:
        model = ProductServiceRelationship
        fields = ('product', 'name', 'quantity')


class ServiceSerializer(serializers.ModelSerializer):
    product = ProductServiceRelationshipSerializer(source='productservicerelationship_set', many=True)
    class Meta:
        model = Service
        fields = ('id', 'harvest', 'name', 'initial_date', 'end_date', 'total_cost', 'product')
    
    def create(self, validated_data):
        product_data = validated_data.pop('productservicerelationship_set')
        service = Service.objects.create(**validated_data)
        for product in product_data:
            d=dict(product)
            prodrel = ProductServiceRelationship.objects.create(service=service,
                                                                product=d['product'],
                                                                quantity=d['quantity'])
            service.productservicerelationship_set.add(prodrel)
        return service



class HarvestSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Harvest
        fields = ('id', 'name', 'initial_date', 'end_date', 'services')