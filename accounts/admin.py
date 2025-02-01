from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'department', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'department')
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional info'), {'fields': ('phone', 'department')}),
    ) 