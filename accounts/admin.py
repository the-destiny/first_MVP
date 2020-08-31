from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):
    # change_list view
    list_display = (
        '__str__',
        'username',
    )
    list_filter = (
        'is_subscriber',
    )
    search_fields = (
        'username',
    )
    ordering = (
        '-is_subscriber',
        'username',
    )

    # change view
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
                'email',
                'lecture_count',
                'is_subscriber',
                'is_active',
            )
        }),
        ('권한', {
            'fields': (
                'is_staff',
                'is_superuser',
            ),
        }),
    )
