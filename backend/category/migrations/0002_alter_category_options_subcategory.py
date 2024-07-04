# Generated by Django 5.0.6 on 2024-07-03 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("name",),
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Subcategory",
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
                    "categories",
                    models.ManyToManyField(
                        related_name="subcategories",
                        to="category.category",
                        verbose_name="Категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Подкатегория",
                "verbose_name_plural": "Подкатегории",
                "ordering": ("name",),
                "abstract": False,
            },
        ),
    ]