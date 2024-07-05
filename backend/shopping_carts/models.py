from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product


User = get_user_model()


class ShoppingCart(models.Model):
    '''ShoppingCart model.'''
    user = models.OneToOneField(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='shopping_cart',
    )
    products = models.ManyToManyField(
        Product,
        through='CartItem',
        verbose_name='Товары',
        related_name='shopping_carts',
    )
    # toal_price = 
    #created #updated

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина №{self.id}'


class CartItem(models.Model):
    '''Cart item model.'''
    shopping_cart = models.ForeignKey(
        ShoppingCart,
        verbose_name='Корзина',
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Товар',
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество',
    )
    total_price = models.DecimalField(
        verbose_name='Цена',
        max_digits=8,
        decimal_places=2,
        # validators=(MinValueValidator(limit_value=0),)
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
