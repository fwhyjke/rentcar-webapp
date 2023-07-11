from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Django admin interface configuration for 'User'
class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ['email']
    # fields which will displayed into User list in admin
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_verified')
    # This is required for correct operation
    readonly_fields = ('date_joined',)
    # Settings for the editor of user
    fieldsets = (
        ('Email & PW', {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_verified')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Settings for the user creation page
    add_fieldsets = (
        ('New user <3', {'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff'),
                         'description': 'Create a new user'}),
    )
    # Fields to filter by
    list_filter = ('is_staff', 'date_joined')


admin.site.register(User, CustomUserAdmin)
