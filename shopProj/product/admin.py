from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)