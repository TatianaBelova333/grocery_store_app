# Generated by Django 5.0.6 on 2024-07-04 13:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                    "name",
                    models.CharField(
                        db_index=True,
                        max_length=200,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=200, unique=True, verbose_name="slug"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to="category/images/",
                        verbose_name="Избражение",
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание продукта")),
                (
                    "price_per_unit",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="Цена"
                    ),
                ),
                (
                    "discount",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(limit_value=100)
                        ],
                        verbose_name="Скидка",
                    ),
                ),
                (
                    "unit",
                    models.CharField(
                        choices=[
                            ("кг", "кг"),
                            ("г", "г"),
                            ("шт", "шт"),
                            ("л", "л"),
                            ("мл", "мл"),
                        ],
                        default="шт",
                        max_length=2,
                        verbose_name="Единица товара",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ("name",),
                "abstract": False,
            },
        ),
    ]
