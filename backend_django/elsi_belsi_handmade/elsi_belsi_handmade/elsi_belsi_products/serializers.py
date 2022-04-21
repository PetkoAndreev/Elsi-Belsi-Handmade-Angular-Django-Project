from rest_framework import serializers
from elsi_belsi_handmade.elsi_belsi_products.models import Product


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'prd_category', 'prd_description', 'prd_image', 'prd_price']


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'prd_category', 'prd_description', 'prd_image', 'prd_price']

    def create(self, validated_data):
        validated_data['prd_user'] = self.context['request'].user
        return super().create(validated_data)


class ProductGetUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'prd_category', 'prd_description', 'prd_image', 'prd_price', 'likes', 'favorites']
        # depth = 2

    # Added logic for patch request
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.partial_update(request, *args, **kwargs)
