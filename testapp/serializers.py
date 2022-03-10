from uuid import UUID
from rest_framework import serializers
from .models import Cart, Reviews

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'name', 'description', 'product']

class CartSerializers(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Cart
        fields = ['id']