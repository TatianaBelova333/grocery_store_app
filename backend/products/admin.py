from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin panel for the Category model.'''

    list_display = (
        'id',
        'name',
        'subcategory_link',
        'description',
        'unit',
        'unit_price',
        'discount',
        'discounted_price',
        'is_in_stock',
        'quantity',
        'created',
        'updated',
    )
    list_filter = (
        'subcategory',
    )

    def subcategory_link(self, obj):
        subcategory = obj.subcategory
        url = reverse(
            'admin:category_subcategory_changelist'
        ) + str(subcategory.id)
        return format_html(f'<a href="{url}">{subcategory}</a>')

    subcategory_link.short_description = 'Подкатегория'
