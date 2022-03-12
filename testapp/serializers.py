from ast import Try
from pprint import pprint
from uuid import UUID
from numpy import product
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


class AddProductCartSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError('Product does not exist')
        return value


    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']
    
    def save(self, **kwargs):
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        cart_id = self.context['cart_id']
        
        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            # update an existing item
            print(cart_item)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            # Create a new item
            print('create a new item', cart_id, product_id, quantity)
            CartItem.objects.create(cart_id=cart_id, **self.validated_data)

        return self.instance