from django.shortcuts import render

from rest_framework import viewsets
# from cart.models import Cart,CartItem
from .serializer import CartItemSerializer,CartSerializer
from cart.models import CartItem,Cart


# Create your views here.

class CartItemView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class =CartItemSerializer


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class =CartSerializer

