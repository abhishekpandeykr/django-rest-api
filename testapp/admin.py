from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.

class CustomCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')

class CustomCartItemAdmin(admin.ModelAdmin):
    list_displays = ['cart.id', 'product.id', 'quantity']

admin.site.register(Cart, CustomCartAdmin)
admin.site.register(CartItem, CustomCartItemAdmin)