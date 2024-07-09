from django.contrib.auth.models import AbstractUser
from django.db import models

from category.models import DatesModelMixin
from products.models import Product


class User(AbstractUser):
    '''User Class.'''

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class ShoppingCart(DatesModelMixin):
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
    quantity = models.DecimalField(
        verbose_name='Количество',
        max_digits=6,
        decimal_places=3,
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        constraints = [
            models.UniqueConstraint(
                fields=('shopping_cart', 'product'),
                name='unique_cart_product',
            )
        ]
