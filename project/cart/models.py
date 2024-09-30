from django.db import models

from users.models import Users
from product.models import Product

# class Product(models.Model):
#     id=models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)


# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     # stock = models.IntegerField()
#     image = models.ImageField(upload_to='product_images/', null=True, blank=True)
#
#     def __str__(self):
#         return self.name



class Cart(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)




class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


