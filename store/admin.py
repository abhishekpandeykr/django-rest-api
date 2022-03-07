from django.contrib import admin
from .models import Product

class CustomProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_per_unit', 'slug')
    list_filter = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product, CustomProductAdmin)
# Register your models here.
