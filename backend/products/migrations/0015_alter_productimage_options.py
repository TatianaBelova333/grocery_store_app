# Generated by Django 5.0.6 on 2024-07-08 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0014_productimage_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productimage",
            options={
                "default_related_name": "images",
                "verbose_name": "Фото товара",
                "verbose_name_plural": "Фото товаров",
            },
        ),
    ]
