from django.contrib import admin
from .models import Resume, ResumeAnalysis

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'uploaded_at', 'status')
    list_filter = ('status', 'uploaded_at')
    search_fields = ('title', 'uploaded_by__username')
    readonly_fields = ('uploaded_at',)

@admin.register(ResumeAnalysis)
class ResumeAnalysisAdmin(admin.ModelAdmin):
    list_display = ('resume', 'created_at')
    readonly_fields = ('created_at',) 