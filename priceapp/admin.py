from django.contrib import admin
from .models import Product, PriceHistory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'last_flipkart_price', 'last_amazon_price', 'created_at', 'updated_at')
    search_fields = ('name', 'user__username')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    
@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'store', 'checked_at')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
