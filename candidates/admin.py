from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Candidate, Evaluation

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('created_at',)

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'score', 'created_at')
    list_filter = ('score', 'created_at')
    search_fields = ('candidate__name', 'comments') 