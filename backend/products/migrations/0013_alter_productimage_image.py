# Generated by Django 5.0.6 on 2024-07-08 21:59

import category.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0012_alter_productimage_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimage",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=category.utils.images_directory_path
            ),
        ),
    ]
