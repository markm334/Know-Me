from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Wishlist, Farmer

# Helper: Allow only superuser
class SuperUserOnlyMixin:
    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

@admin.register(Product)
class ProductAdmin(SuperUserOnlyMixin, admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'deposit_percentage', 'thumbnail')
    search_fields = ('name',)
    list_filter = ('price',)

    def thumbnail(self, obj):
        if hasattr(obj, 'image') and obj.image:
            return format_html('<img src="{}" style="max-height:50px;"/>', obj.image.url)
        return "-"

@admin.register(Wishlist)
class WishlistAdmin(SuperUserOnlyMixin, admin.ModelAdmin):
    list_display = ('product', 'added_on')
    list_filter = ('added_on',)

@admin.register(Farmer)
class FarmerAdmin(SuperUserOnlyMixin, admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'location')
    search_fields = ('name', 'email')
