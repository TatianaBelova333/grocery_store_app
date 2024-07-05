from rest_framework import serializers
from category.models import Category

from products.models import Product


class ProductCatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
        )


class ProductSubCatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
        )


class ProductSerializer(serializers.ModelSerializer):
    '''Serializer for products.'''
    categories = ProductCatSerializer(
        source='subcategory.categories',
        many=True,
    )
    subcategory = ProductSubCatSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'categories',
            'subcategory',
            'unit_price',
            'unit',
            'in_stock',
            'quantity',
        )
