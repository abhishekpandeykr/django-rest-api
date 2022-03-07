from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

# create product list view
@api_view()
def product_list(request):
    product_query_set = Product.objects.all()
    serializer = ProductSerializer(product_query_set, many=True)
    return Response(serializer.data)

@api_view()
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
