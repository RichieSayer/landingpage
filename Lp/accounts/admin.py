from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Customize the admin display as needed (list_display, fieldsets, etc.)
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth','phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth','phone_number')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)