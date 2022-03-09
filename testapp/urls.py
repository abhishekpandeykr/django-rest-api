#  import pathlib
# from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import ProductViewSets

custom_router = SimpleRouter()
custom_router.register('products', ProductViewSets)

urlpatterns = custom_router.urls
