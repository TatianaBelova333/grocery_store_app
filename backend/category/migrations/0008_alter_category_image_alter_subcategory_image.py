# Generated by Django 5.0.6 on 2024-07-08 22:00

import category.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0007_category_image_category_slug_subcategory_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=category.utils.images_directory_path
            ),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=category.utils.images_directory_path
            ),
        ),
    ]