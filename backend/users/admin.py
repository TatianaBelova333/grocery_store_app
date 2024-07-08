from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'shopping_cart'
    )
    list_filter = ('email', 'username')
    search_fields = ('email', 'first_name', 'last_name', 'username')
    readonly_fields = ('last_login', 'date_joined')
    fieldsets = (
        (None, {'fields': (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            "is_active",
            'last_login',
            'date_joined',
        )}),
    )
