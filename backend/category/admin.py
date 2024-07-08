from django.contrib import admin

from category.models import Category, Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin panel for the Category model.'''

    list_display = (
        'id',
        'name',
        'slug',
        'image',
        'created',
        'updated',
    )


@admin.register(Subcategory)
class CaSubcategoryAdmin(admin.ModelAdmin):
    '''Admin panel for the Subcategory model.'''

    list_display = (
        'id',
        'name',
        'slug',
        'image',
        'display_categories',
        'created',
        'updated',
    )
