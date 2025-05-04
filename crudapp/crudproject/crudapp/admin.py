from django.contrib import admin
from .models import Product, Wishlist, Farmer

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'deposit_percentage')
    search_fields = ('name',)
    list_filter = ('price',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('product', 'added_on')
    list_filter = ('added_on',)

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'location')
    search_fields = ('name', 'email')