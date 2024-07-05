# Generated by Django 5.0.6 on 2024-07-05 07:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0003_remove_product_price_per_unit_product_in_stock_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveSmallIntegerField(verbose_name="Количество"),
                ),
                (
                    "total_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="Цена"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                        verbose_name="Товар",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShoppingCart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        related_name="shopping_carts",
                        through="shopping_carts.Item",
                        to="products.product",
                        verbose_name="Товары",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shopping_cart",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="item",
            name="shopping_cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="shopping_carts.shoppingcart",
                verbose_name="Корзина",
            ),
        ),
    ]
