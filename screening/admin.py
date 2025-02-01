from django.contrib import admin
from .models import JobDescription, ScreeningTask

@admin.register(JobDescription)
class JobDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)

@admin.register(ScreeningTask)
class ScreeningTaskAdmin(admin.ModelAdmin):
    list_display = ('job', 'created_by', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    readonly_fields = ('created_at',) 