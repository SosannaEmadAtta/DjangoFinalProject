from django.urls import path
from . import views
# from cart.api.serializers import CartItemSerializer
# from cart.api.views import add_cart, get_cart

app_name ='cart'
urlpatterns = [
    path('create/', views.create_product, name='create'),
    path('list/',views.list_products,name='list'),
]