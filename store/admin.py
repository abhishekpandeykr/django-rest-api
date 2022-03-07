from django.contrib import admin
from .models import Product, Collection

class CustomProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_per_unit', 'slug')
    list_filter = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class CustomCollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'feature_product', 'id')

admin.site.register(Product, CustomProductAdmin)
admin.site.register(Collection, CustomCollectionAdmin)
# Register your models here.
