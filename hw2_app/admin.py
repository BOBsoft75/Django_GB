from django.contrib import admin
from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'date_registration')
    search_fields = ('name', 'email', 'phone', 'address')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'store', 'date_receipt')
    list_filter = ('store', 'date_receipt')
    search_fields = ('name', 'description')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client', 'total_amount', 'date_order')
    search_fields = ('pk', 'client', 'product', 'total_amount', 'date_order')