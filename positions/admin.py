from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'status', 'created_at')
    list_filter = ('status', 'department', 'created_at')
    search_fields = ('title', 'department', 'description', 'requirements')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        (None, {
            'fields': ('title', 'department', 'status')
        }),
        (_('详细信息'), {
            'fields': ('description', 'requirements'),
            'classes': ('collapse',)
        }),
    ) 