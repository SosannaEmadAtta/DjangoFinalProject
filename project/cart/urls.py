
from django.urls import path
from . import views
# from cart.api.serializers import CartItemSerializer
# from cart.cart_api.views import CartItemListCreateView
# from cart.api.views import add_cart, get_cart
# from .models import CartItem
# from cart.cart_api.views import CartItemListCreateView
# from .views import CartItemListCreateView
# from .serializers import CartItemSerializer
app_name ='cart'
urlpatterns = [
    # path('create_product/', views.create_product, name='create_product'),
    # path('list_products/',views.list_products,name='list_products'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('cart_detail/',views.cart_detail,name='cart_detail'),
    path('inc_quantity/<int:product_id>/',views.inc_quantity,name='inc_quantity'),
    path('dec_quantity/<int:product_id>/',views.dec_quantity,name='dec_quantity'),
    # path('Add/',CartItemListCreateView.as_view(),name='add_item'),
    # path('add/',add_cart,name='add_item'),
    # path('get/',get_cart,name='get_item'),
]