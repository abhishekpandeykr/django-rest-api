from rest_framework import serializers
from .models import Reviews

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'name', 'description', 'product']