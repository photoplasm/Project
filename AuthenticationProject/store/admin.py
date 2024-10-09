from django.contrib import admin
from .models import Product
from .models import Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_url')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'payment_method',)