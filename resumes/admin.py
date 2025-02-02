from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from .models import (
    Resume, Education, WorkExperience, 
    ResumeAnalysis, ResumeSearch
)


class EducationInline(admin.TabularInline):
    """教育经历内联管理"""
    model = Education
    extra = 0
    fields = ['school', 'major', 'degree', 'start_date', 'end_date', 'gpa']


class WorkExperienceInline(admin.TabularInline):
    """工作经历内联管理"""
    model = WorkExperience
    extra = 0
    fields = ['company', 'position', 'start_date', 'end_date', 'description']


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    """简历管理"""
    list_display = [
        'name', 'title', 'email', 'phone', 'status', 
        'job_intention', 'upload_time', 'file_download'
    ]
    list_filter = ['status', 'upload_time', 'job_status']
    search_fields = ['name', 'title', 'email', 'phone', 'job_intention']
    readonly_fields = ['upload_time', 'uploader']
    inlines = [EducationInline, WorkExperienceInline]
    
    fieldsets = [
        (_('基本信息'), {
            'fields': (
                'title', 'file', 'file_type', 'status',
                'upload_time', 'uploader'
            )
        }),
        (_('个人信息'), {
            'fields': (
                'name', 'email', 'phone', 'gender',
                'birth_date', 'current_location'
            )
        }),
        (_('求职信息'), {
            'fields': (
                'job_intention', 'expected_salary', 'job_status'
            )
        }),
    ]
    
    def file_download(self, obj):
        """文件下载链接"""
        if obj.file:
            return format_html(
                '<a href="{}" target="_blank">下载</a>',
                obj.file.url
            )
        return '-'
    file_download.short_description = _('下载')

    def save_model(self, request, obj, form, change):
        """保存时自动设置上传者"""
        if not change:  # 仅在创建时设置
            obj.uploader = request.user
        super().save_model(request, obj, form, change)

    def has_module_permission(self, request):
        """确保用户有查看模块的权限"""
        return request.user.has_perm('resumes.view_resume')

    def has_add_permission(self, request):
        """确保用户有添加简历的权限"""
        return request.user.has_perm('resumes.add_resume')

    def has_change_permission(self, request, obj=None):
        """确保用户有修改简历的权限"""
        return request.user.has_perm('resumes.change_resume')

    def has_delete_permission(self, request, obj=None):
        """确保用户有删除简历的权限"""
        return request.user.has_perm('resumes.delete_resume')

    def has_view_permission(self, request, obj=None):
        """确保用户有查看简历的权限"""
        return request.user.has_perm('resumes.view_resume')


@admin.register(ResumeAnalysis)
class ResumeAnalysisAdmin(admin.ModelAdmin):
    """简历解析管理"""
    list_display = [
        'resume', 'experience_years', 'education_level',
        'last_company', 'last_position', 'analysis_time'
    ]
    list_filter = ['analysis_time', 'education_level']
    search_fields = [
        'resume__name', 'resume__title',
        'last_company', 'last_position'
    ]
    readonly_fields = ['analysis_time']
    
    fieldsets = [
        (_('基本信息'), {
            'fields': ('resume', 'analysis_time')
        }),
        (_('解析结果'), {
            'fields': (
                'experience_years', 'education_level',
                'last_company', 'last_position'
            )
        }),
        (_('详细信息'), {
            'fields': ('parsed_content', 'skills'),
            'classes': ('collapse',)
        }),
    ]


@admin.register(ResumeSearch)
class ResumeSearchAdmin(admin.ModelAdmin):
    """简历检索管理"""
    list_display = [
        'user', 'query', 'results_count', 'search_time'
    ]
    list_filter = ['search_time', 'user']
    search_fields = ['query', 'user__username']
    readonly_fields = ['search_time']
    
    fieldsets = [
        (_('搜索信息'), {
            'fields': (
                'user', 'query', 'filters',
                'results_count', 'search_time'
            )
        }),
    ]

    def has_add_permission(self, request):
        """禁止手动添加搜索记录"""
        return False
    