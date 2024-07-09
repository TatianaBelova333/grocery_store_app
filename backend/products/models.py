from decimal import Decimal
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from category.models import (
    BaseImage,
    DatesModelMixin,
    NameBaseModel,
    SlugBaseModel,
    Subcategory
)


class ProductImage(BaseImage):
    """Image model for product images."""
    product = models.ForeignKey(
        'Product',
        verbose_name='Товар',
        on_delete=models.CASCADE,
        related_name='images'
    )

    class Meta(BaseImage.Meta):
        verbose_name = "Фото товара"
        verbose_name_plural = "Фото товаров"
        constraints = [
            models.UniqueConstraint(
                fields=('product', 'image'),
                name='image',
            )
        ]

    def __str__(self):
        return f"products/{self.product.slug}"


class Country(NameBaseModel):
    '''Country of manufacture model.'''

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Страна производителя'
        verbose_name_plural = 'Страны производителей'


class Brand(NameBaseModel):
    '''Brand model.'''

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Product(SlugBaseModel, DatesModelMixin):
    '''Product model.'''
    class MeaurementUnit(models.TextChoices):
        KG = ('кг', 'кг')
        PC = ('шт', 'шт')
        L = ('л', 'л')

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
        validators=(MinValueValidator(limit_value=0.00),)
    )
    discount = models.PositiveSmallIntegerField(
        verbose_name='Скидка',
        validators=(MaxValueValidator(limit_value=100),),
        default=0,
    )
    unit = models.CharField(
        verbose_name='Единица товара',
        max_length=2,
        choices=MeaurementUnit.choices,
        default=MeaurementUnit.PC,
    )
    stock_quantity = models.DecimalField(
        verbose_name='Длступное кол-во',
        max_digits=6,
        decimal_places=3,
        validators=(MinValueValidator(limit_value=0.100),)
    )
    country = models.ForeignKey(
        Country,
        verbose_name='Страна производства',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )
    brand = models.ForeignKey(
        Brand,
        verbose_name='Бренд',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )
    loose = models.BooleanField(
        verbose_name='На развес',
        default=False,
    )

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def is_in_stock(self):
        return bool(self.stock_quantity > 0)

    def discounted_price(self):
        return Decimal((self.unit_price)*(100 - self.discount)/100)

    discounted_price.short_description = 'Цена со скидкой'
    is_in_stock.short_description = 'В наличии'
    is_in_stock.boolean = True
