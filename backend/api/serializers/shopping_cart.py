from decimal import Decimal
from django.shortcuts import get_object_or_404

from django.utils import timezone
from django.db import DatabaseError, transaction
from django.db.models import F, Sum
from rest_framework import serializers

from products.models import Product
from users.models import CartItem, ShoppingCart


class CartItemCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = (
            'id',
            'shopping_cart',
            'product',
            'quantity',
        )
        read_only_fields = ('id', 'shopping_cart', 'product')

    def validate_quantity(self, quantity):
        '''
        Validate that the requested item quantity does not exceed
        the available product quantity.

        '''
        view = self.context['view']
        product_id = view.kwargs['pk']
        product = get_object_or_404(Product, pk=product_id)
        if not product.loose:
            if Decimal(quantity) != int(quantity):
                raise serializers.ValidationError(
                    ('Данный товар продается поштучно. '
                     'Количество должно быть целым числом.')
                )
        if product.stock_quantity < quantity:
            raise serializers.ValidationError(
                    'Недостаточное количество на складе.'
                )
        return quantity

    def create(self, validated_data):
        try:
            with transaction.atomic():
                cart_item = CartItem.objects.create(**validated_data)
                shopping_cart = cart_item.shopping_cart
                shopping_cart.updated = timezone.now()
                shopping_cart.save()
        except DatabaseError:
            raise serializers.ValidationError(
                'Ошибка добавления товара в корзину.'
            )

        return cart_item


class ProductBriefInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'unit',
            'unit_price',
            'discounted_price',
            'stock_quantity',
        )


class CartItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()
    product = ProductBriefInfoSerializer()
    quantity = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = (
            'id',
            'product',
            'quantity',
            'subtotal',
        )

    def get_subtotal(self, obj):
        item_price = obj.product.unit_price
        discount = obj.product.discount
        if discount > 0:
            item_price *= Decimal(100 - discount) / 100

        total_price = Decimal(item_price * obj.quantity)

        return total_price

    def get_quantity(self, obj):
        """Check if the product stock quantity is still available."""
        if obj.product.stock_quantity < obj.quantity:
            obj.quantity = obj.product.stock_quantity
            obj.save()
        return obj.quantity


class ShoppingCartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    total = serializers.DecimalField(max_digits=8, decimal_places=2)
    cart_id = serializers.IntegerField(source='id')
    total = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingCart
        fields = (
            'cart_id',
            'items',
            'total',
        )

    def get_total(self, cart):
        cart_with_total = cart.items.aggregate(
            total=Sum(
                (F('quantity') * F('product__unit_price')
                    * (100 - F('product__discount')) / 100)
                )
            )
        return Decimal(cart_with_total['total'])
