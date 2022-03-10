from django.shortcuts import render
from store.serializers import ProductSerializer, CollectionSerializer
from store.models import Product, Collection
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from testapp.models import Reviews
from testapp.serializers import ReviewSerializers
from .filter import ProductFilter
# Create your views here.

class ProductViewSets(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_serializer_context(self):
        return {'request':self.request}
    


class CollectionViewSets(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class ReviewsViewSets(ModelViewSet):
    # queryset = Reviews.objects.all()
    serializer_class = ReviewSerializers

    def get_queryset(self):
        return Reviews.objects.filter(product_id=self.kwargs['products_pk'])
