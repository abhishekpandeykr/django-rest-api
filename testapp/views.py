from django.shortcuts import render
from store.serializers import ProductSerializer, CollectionSerializer
from store.models import Product, Collection
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin

from testapp.models import Reviews, Cart, CartItem
from testapp.serializers import CartSerializers, ReviewSerializers, CartItemSerializers
from .filter import ProductFilter
from .pagination import DefaultPagination
# Create your views here.

class ProductViewSets(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price_per_unit', 'created_at']
    pagination_class = DefaultPagination

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


class CartViewSets(CreateModelMixin,RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers


class CartItemViewSets(ModelViewSet):
    queryset = CartItem.objects.prefetch_related('cart_items__product').all()
    serializer_class = CartItemSerializers
