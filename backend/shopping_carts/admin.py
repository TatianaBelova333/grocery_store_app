from django.contrib import admin

from shopping_carts.models import CartItem, ShoppingCart


class CartItemInline(admin.TabularInline):
    model = CartItem
    raw_id_fields = ('shopping_cart',)
    min_num = 0


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    '''Admin panel for the ShoppingCart model.'''

    list_display = (
        'id',
        'user',
    )
    inlines = (CartItemInline,)
