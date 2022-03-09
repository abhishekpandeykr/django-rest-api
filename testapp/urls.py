#  import pathlib
# from django.urls import path, include
from rest_framework_nested import routers
from .views import CollectionViewSets, ProductViewSets, ReviewsViewSets

custom_router = routers.DefaultRouter()
custom_router.register('products', ProductViewSets)
custom_router.register('collection', CollectionViewSets)

product_router = routers.NestedDefaultRouter(custom_router, 'products', lookup='products')
product_router.register('reviews', ReviewsViewSets, basename="product-reviews")

urlpatterns = custom_router.urls + product_router.urls
