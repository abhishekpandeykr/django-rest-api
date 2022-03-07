from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('title',)


class Collection(models.Model):
    title = models.CharField(max_length=255)
    feature_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True, related_name='feature_product')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('title',)