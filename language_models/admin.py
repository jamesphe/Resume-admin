from django.contrib import admin
from .models import LanguageModel

@admin.register(LanguageModel)
class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'model_type', 'is_active')
    list_filter = ('model_type', 'is_active')
    search_fields = ('name',) 