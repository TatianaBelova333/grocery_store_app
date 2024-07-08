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
    in_cart = serializers.BooleanField()
    discounted_price = serializers.DecimalField(max_digits=8, decimal_places=2)
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'categories',
            'subcategory',
            'unit_price',
            'discounted_price',
            'discount',
            'unit',
            'quantity',
            'in_cart',
        )

    def get_discount(self, obj):
        return f'{obj.discount}%'
