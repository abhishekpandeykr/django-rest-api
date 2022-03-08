from django.urls import path
from . import views

urlpatterns = [
    path('products', views.product_list, name='product_list'),
    path('products/<int:pk>', views.product_detail, name='product_detail'),
    path('class/product-list', views.ProductList.as_view(), name='product_list_class'),
    path('generics/product-list', views.ProcutListWithGenerics.as_view(), name='product_list_generics'),
    path('generics/products/<int:pk>', view=views.ProductDetail.as_view(), name='product_detail_generics'),
]