from django.shortcuts import render
from rest_framework import viewsets
from product.models import Product
from .serializer import ProductSerializer

# Create your views here.

class ProductView(viewsets.ModelViewSet):
     queryset=Product.objects.all()
     serializer_class = ProductSerializer

def test(request):
    return HttpResponse('hello')