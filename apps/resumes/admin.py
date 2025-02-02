from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'education', 'school', 'major', 'created_at')
    list_filter = ('education', 'created_at')
    search_fields = ('name', 'school', 'major', 'skills')
    readonly_fields = ('vector_id', 'created_at', 'updated_at')
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'phone', 'email', 'education')
        }),
        ('教育背景', {
            'fields': ('school', 'major')
        }),
        ('专业技能', {
            'fields': ('work_experience', 'skills')
        }),
        ('文件信息', {
            'fields': ('file',)
        }),
        ('系统信息', {
            'fields': ('vector_id', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    ) 