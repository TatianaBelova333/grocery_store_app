from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from products.models import Brand, Country, Product, ProductImage


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    '''Admin panel for the Brand model.'''

    list_display = (
        'id',
        'name',
    )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    '''Admin panel for the Country model.'''

    list_display = (
        'id',
        'name',
    )


class ImageInLine(admin.TabularInline):
    model = ProductImage
    raw_id_fields = ("product",)
    max_num = 3
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin panel for the Category model.'''

    list_display = (
        'id',
        'name',
        'subcategory_link',
        'description',
        'unit',
        'loose',
        'unit_price',
        'discount',
        'discounted_price',
        'is_in_stock',
        'stock_quantity',
        'country',
        'brand',
        'created',
        'updated',
    )
    list_filter = (
        'subcategory',
    )
    inlines = (ImageInLine,)

    def subcategory_link(self, obj):
        subcategory = obj.subcategory
        url = reverse(
            'admin:category_subcategory_changelist'
        ) + str(subcategory.id)
        return format_html(f'<a href="{url}">{subcategory}</a>')

    subcategory_link.short_description = 'Подкатегория'
