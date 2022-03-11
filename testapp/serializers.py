from pprint import pprint
from uuid import UUID
from rest_framework import serializers

from store.models import Product
from .models import Cart, Reviews, CartItem

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price_per_unit']

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'name', 'description', 'product']


class CartItemSerializers(serializers.ModelSerializer):
    product = SimpleProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart_item):
        return cart_item.product.price_per_unit * cart_item.quantity
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'total_price']


class CartSerializers(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    cart_items = CartItemSerializers(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart):
        return sum([item.quantity * item.product.price_per_unit for item in cart.cart_items.all()])
        
    class Meta:
        model = Cart
        fields = ['id', 'cart_items', 'total_price']