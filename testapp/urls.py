#  import pathlib
# from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import CollectionViewSets, ProductViewSets

custom_router = SimpleRouter()
custom_router.register('products', ProductViewSets)
custom_router.register('collection', CollectionViewSets)

urlpatterns = custom_router.urls
