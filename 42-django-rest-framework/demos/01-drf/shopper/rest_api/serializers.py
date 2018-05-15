from rest_framework import serializers
from shopper_products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'cover', 'name', 'description', 'price')
