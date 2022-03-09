from django.shortcuts import render
from store.serializers import ProductSerializer, CollectionSerializer
from store.models import Product, Collection
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class ProductViewSets(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request':self.request}


class CollectionViewSets(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

