#  import pathlib
# from django.urls import path, include
from rest_framework_nested import routers
from .views import CollectionViewSets, ProductViewSets, ReviewsViewSets, CartViewSets, CartItemViewSets

custom_router = routers.DefaultRouter()
custom_router.register('products', ProductViewSets, basename='products')
custom_router.register('collection', CollectionViewSets)
custom_router.register('cart', CartViewSets, basename="product-cart")

product_router = routers.NestedDefaultRouter(custom_router, 'products', lookup='products')
product_router.register('reviews', ReviewsViewSets, basename="product-reviews")


urlpatterns = custom_router.urls + product_router.urls 
