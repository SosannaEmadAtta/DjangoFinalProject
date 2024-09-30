from rest_framework import serializers
from cart.models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)  # Show product name

    class Meta:
        model = CartItem
        fields = ['product_id', 'quantity','cart_id','product']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at','is_paid','items']