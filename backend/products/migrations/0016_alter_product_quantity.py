# Generated by Django 5.0.6 on 2024-07-09 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0015_alter_productimage_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(verbose_name="Количество"),
        ),
    ]