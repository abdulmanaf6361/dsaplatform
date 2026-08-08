from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'batch_name', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Batch Info', {'fields': ('batch_name', 'is_trainer')}),
    )
