from decimal import Decimal
from django.shortcuts import get_object_or_404

from django.utils import timezone
from django.db import DatabaseError, transaction
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

    def validate(self, data):
        '''
        Validate that the requested item quantity does not exceed
        the available product quantity.

        '''
        view = self.context['view']
        product_id = view.kwargs['pk']
        product = get_object_or_404(Product, pk=product_id)
        item_quantity = data['quantity']
        if product.quantity < item_quantity:
            raise serializers.ValidationError(
                    'Товар закончился или отсутствует необходимое количество.'
                )
        return data

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


class CartItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()

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


class ShoppingCartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    total = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = ShoppingCart
        fields = (
            'id',
            'items',
            'total',
        )
