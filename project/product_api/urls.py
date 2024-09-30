from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductView

router = DefaultRouter()
router.register(r'products', ProductView)  # Register the Product viewset

urlpatterns = [
    path('', include(router.urls)),  # Include the router-generated URLs
]