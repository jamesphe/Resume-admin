from rest_framework import serializers
from .models import (
    Resume, Education, WorkExperience, 
    ResumeAnalysis, ResumeSearch
)


class EducationSerializer(serializers.ModelSerializer):
    """教育经历序列化器"""
    
    class Meta:
        model = Education
        fields = [
            'id', 'school', 'major', 'degree',
            'start_date', 'end_date', 'gpa'
        ]


class WorkExperienceSerializer(serializers.ModelSerializer):
    """工作经历序列化器"""
    
    class Meta:
        model = WorkExperience
        fields = [
            'id', 'company', 'position',
            'start_date', 'end_date', 'description'
        ]


class ResumeAnalysisSerializer(serializers.ModelSerializer):
    """简历解析序列化器"""
    
    class Meta:
        model = ResumeAnalysis
        fields = [
            'id', 'parsed_content', 'skills',
            'experience_years', 'education_level',
            'last_company', 'last_position',
            'analysis_time'
        ]
        read_only_fields = ['analysis_time']


class ResumeSerializer(serializers.ModelSerializer):
    """简历序列化器"""
    
    educations = EducationSerializer(many=True, read_only=True)
    work_experiences = WorkExperienceSerializer(many=True, read_only=True)
    analysis = ResumeAnalysisSerializer(read_only=True)
    file_url = serializers.URLField(source='file.url', read_only=True)
    uploader_name = serializers.CharField(
        source='uploader.username', 
        read_only=True
    )

    class Meta:
        model = Resume
        fields = [
            'id', 'title', 'file', 'file_url', 'file_type',
            'status', 'uploader', 'uploader_name', 'upload_time',
            'name', 'email', 'phone', 'gender', 'birth_date',
            'current_location', 'job_intention', 'expected_salary',
            'job_status', 'educations', 'work_experiences',
            'analysis'
        ]
        read_only_fields = ['upload_time', 'uploader']


class ResumeSearchSerializer(serializers.ModelSerializer):
    """简历检索序列化器"""
    
    user_name = serializers.CharField(
        source='user.username', 
        read_only=True
    )

    class Meta:
        model = ResumeSearch
        fields = [
            'id', 'user', 'user_name', 'query',
            'filters', 'results_count', 'search_time'
        ]
        read_only_fields = ['search_time', 'user'] 