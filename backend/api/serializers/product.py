from rest_framework import serializers

from category.models import Category
from products.models import Product, ProductImage


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


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ('image',)


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
    country = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    images = ImageSerializer(many=True)
    qty_in_cart = serializers.DecimalField(max_digits=6, decimal_places=3)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'images',
            'categories',
            'subcategory',
            'description',
            'country',
            'brand',
            'unit_price',
            'discounted_price',
            'discount',
            'unit',
            'stock_quantity',
            'in_cart',
            'qty_in_cart'
        )

    def get_discount(self, obj):
        return f'{obj.discount}%'
