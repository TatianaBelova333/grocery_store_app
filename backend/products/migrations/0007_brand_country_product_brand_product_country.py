# Generated by Django 5.0.6 on 2024-07-08 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_remove_product_image_remove_product_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
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
            ],
            options={
                "verbose_name": "Бренд",
                "verbose_name_plural": "Бренды",
                "ordering": ("name",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Country",
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
            ],
            options={
                "verbose_name": "Страна производителя",
                "verbose_name_plural": "Страны производителей",
                "ordering": ("name",),
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="products.brand",
                verbose_name="Бренд",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="country",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="products.country",
                verbose_name="Страна производства",
            ),
        ),
    ]