from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# create product list view
@api_view()
def product_list(request):
    return Response("OK")

@api_view()
def product_detail(request, pk):
    return Response(pk)