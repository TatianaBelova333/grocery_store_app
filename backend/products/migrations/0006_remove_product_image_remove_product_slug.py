# Generated by Django 5.0.6 on 2024-07-08 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_remove_product_in_stock"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
        migrations.RemoveField(
            model_name="product",
            name="slug",
        ),
    ]