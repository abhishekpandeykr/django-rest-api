from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
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


class Employee(models.Model):
    FRONTEND_DEVELOPER = 'FE'
    BACKEND_DEVELOPER = 'BE'
    FULLSTACK_DEVELOPER = 'FS'

    JOB_CHOICES = [(FRONTEND_DEVELOPER, 'Frontend Developer'), (BACKEND_DEVELOPER, 'Backend Developer'),
                     (FULLSTACK_DEVELOPER, 'Fullstack Developer')]
    phone = models.CharField(max_length=10)
    job_type = models.CharField(max_length=2, choices=JOB_CHOICES, default=FRONTEND_DEVELOPER)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
    
    class Meta:
        ordering = ['user__first_name', 'user__last_name']