from django.contrib import admin

# Show data as columns in admin panel
from elsi_belsi_handmade.elsi_belsi_products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name', 'prd_category', 'prd_description', 'prd_price', 'prd_user', 'likes_count',
        'added_to_favorites_count')
    list_filter = ('product_name',)
    sortable_by = ('product_name',)

    # Adding likes to the admin panel
    @staticmethod
    def likes_count(obj):
        return obj.likes.count()

    @staticmethod
    def added_to_favorites_count(obj):
        return obj.likes.count()


admin.site.register(Product, ProductAdmin)
