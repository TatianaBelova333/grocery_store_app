# Generated by Django 5.0.6 on 2024-07-07 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_product_created_product_updated"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="in_stock",
        ),
    ]