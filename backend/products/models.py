from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from category.models import NameBaseModel, Subcategory


class Product(NameBaseModel):
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
    in_stock = models.BooleanField(
        verbose_name='В наличии',
        default=False,
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        default=0,
    )

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
