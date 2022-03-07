from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    price_per_unit = serializers.DecimalField(max_digits=10, decimal_places=2)