from django.contrib import admin
from .models import Candidate


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('resume', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('resume__name', 'notes')
    readonly_fields = ('created_at', 'updated_at') 