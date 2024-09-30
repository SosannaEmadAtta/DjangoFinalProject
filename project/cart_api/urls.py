from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartView,CartItemView

router = DefaultRouter()
router.register(r'carts', CartView)  # Register the Product viewset
router.register(r'cart-items', CartItemView)

urlpatterns = [
    path('', include(router.urls)),  # Include the router-generated URLs

]