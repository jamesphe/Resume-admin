from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import RecruitmentProgress, RecruitmentEffectiveness


@admin.register(RecruitmentProgress)
class RecruitmentProgressAdmin(admin.ModelAdmin):
    list_display = (
        'position',
        'total_candidates',
        'interviewed',
        'passed',
        'report_date'
    )
    list_filter = ('report_date', 'position')
    date_hierarchy = 'report_date'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('position')


@admin.register(RecruitmentEffectiveness)
class RecruitmentEffectivenessAdmin(admin.ModelAdmin):
    list_display = (
        'position',
        'time_to_fill',
        'cost_per_hire',
        'report_date'
    )
    list_filter = ('report_date', 'position')
    date_hierarchy = 'report_date'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('position') 