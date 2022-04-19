from django.contrib import admin

# Show data as columns in admin panel
from elsi_belsi_handmade.elsi_belsi_products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'prd_description', 'prd_category', 'prd_price', 'likes_count')
    list_filter = ('product_name',)
    sortable_by = ('product_name',)

    # Adding likes to the admin panel
    @staticmethod
    def likes_count(obj):
        return obj.like_set.count()


admin.site.register(Product, ProductAdmin)
