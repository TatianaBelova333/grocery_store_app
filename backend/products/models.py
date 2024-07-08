from decimal import Decimal

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from category.models import DatesModelMixin, NameBaseModel, Subcategory


class Product(NameBaseModel, DatesModelMixin):
    '''Product model.'''
    class MeaurementUnit(models.TextChoices):
        KG = ('кг', 'кг')
        G = ('г', 'г')
        PC = ('шт', 'шт')
        L = ('л', 'л')
        ML = ('мл', 'мл')

    subcategory = models.ForeignKey(
        Subcategory,
        verbose_name='Подкатегория',
        on_delete=models.PROTECT,
        related_name='products',
    )
    description = models.TextField(
        verbose_name='Описание продукта',
    )
    unit_price = models.DecimalField(
        verbose_name='Цена за единицу',
        max_digits=8,
        decimal_places=2,
        validators=(MinValueValidator(limit_value=0),)
    )
    discount = models.PositiveSmallIntegerField(
        verbose_name='Скидка',
        validators=(MaxValueValidator(limit_value=100),)
    )
    unit = models.CharField(
        verbose_name='Единица товара',
        max_length=2,
        choices=MeaurementUnit.choices,
        default=MeaurementUnit.PC,
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        default=0,
    )
    # country
    # branc

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def is_in_stock(self):
        return bool(self.quantity > 0)

    def discounted_price(self):
        return Decimal((self.unit_price)*(100 - self.discount)/100)

    discounted_price.short_description = 'Цена со скидкой'
    is_in_stock.short_description = 'В наличии'
    is_in_stock.boolean = True
