from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'location', 'status', 'created_at')
    list_filter = ('status', 'department', 'location')
    search_fields = ('title', 'description', 'requirements')
    readonly_fields = ('created_at', 'updated_at') 