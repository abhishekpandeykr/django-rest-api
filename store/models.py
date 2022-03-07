from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    # category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        ordering = ('title',)


# class Collection(models.Model):
#     title = models.CharField(max_length=255)
#     feature_product = models.ForeignKey('Product', on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return super().__str__()
    
#     class Meta:
#         ordering = ('title',)