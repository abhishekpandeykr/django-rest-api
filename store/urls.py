from django.urls import path
from . import views

urlpatterns = [
    path('products', views.product_list, name='product_list'),
    path('products/<int:pk>', views.product_detail, name='product_detail'),
    path('class/product-list', views.ProductList.as_view(), name='product_list_class'),
]