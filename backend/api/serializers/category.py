from rest_framework import serializers

from category.models import Category, Subcategory


class SubcategorySerializer(serializers.ModelSerializer):
    '''Serializer for product subcategories.'''

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'slug', 'image')


class CategorySerializer(serializers.ModelSerializer):
    '''Serializer for product categories.'''
    image = serializers.ImageField()
    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'subcategories', 'image')
