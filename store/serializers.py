from decimal import Decimal
from rest_framework import serializers

from store.models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price_per_unit')
    price_with_tax = serializers.SerializerMethodField(method_name='get_price_with_tax')

    def get_price_with_tax(self, product:Product):
        return product.price_per_unit * Decimal(1.1)
