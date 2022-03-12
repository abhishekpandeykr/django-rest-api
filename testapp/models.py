from uuid import uuid4
from django.db import models
from django.core.validators import MinValueValidator
from uuid import uuid4
from store.models import Product

# Create your models here.

class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1),
    ])

    class Meta:
        unique_together = [['cart', 'product']]
