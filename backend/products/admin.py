from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin panel for the Category model.'''

    list_display = (
        'id',
        'name',
        'subcategory',
        'description',
        'unit_price',
        'discount',
        'in_stock',
        'quantity',
        'unit',
    )
    list_filter = (
        'subcategory',
    )
