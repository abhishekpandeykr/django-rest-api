from asyncio import constants
from django.contrib import admin
from .models import Product, Collection, Employee

class CustomProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_per_unit', 'slug')
    list_filter = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class CustomCollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'feature_product', 'id')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'job_type']
    # list_display = ['user__first_name', 'user__last_name', 'phone', 'job_type']

    def first_name(self, obj):
        return obj
    
    def last_name(self, obj):
        return obj

admin.site.register(Product, CustomProductAdmin)
admin.site.register(Collection, CustomCollectionAdmin)
admin.site.register(Employee, EmployeeAdmin)
# Register your models here.
