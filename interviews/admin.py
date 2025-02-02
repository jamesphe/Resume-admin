from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Interview


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'position', 'interview_time', 'interview_type', 'status')
    list_filter = ('status', 'interview_type', 'interview_time')
    search_fields = ('candidate__name', 'position__title', 'feedback')
    date_hierarchy = 'interview_time'
    
    fieldsets = (
        (None, {
            'fields': ('candidate', 'position', 'interview_time', 'interview_type', 'status')
        }),
        (_('面试反馈'), {
            'fields': ('feedback',),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('candidate', 'position') 