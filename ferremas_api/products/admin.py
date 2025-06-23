from django.contrib import admin
from .models import Product, Contact

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'brand', 'price', 'created_at')
    search_fields = ('code', 'name', 'brand')
    list_filter = ('brand', 'created_at')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)
