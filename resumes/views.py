from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from .models import Resume, ResumeAnalysis, ResumeSearch
from .serializers import (
    ResumeSerializer, ResumeAnalysisSerializer,
    ResumeSearchSerializer
)

# 暂时为空，因为我们使用的是 admin 接口

@login_required
def resume_list(request):
    resumes = Resume.objects.filter(uploaded_by=request.user)
    return render(request, 'resumes/resume_list.html', {'resumes': resumes})

@login_required
def resume_detail(request, pk):
    resume = Resume.objects.get(pk=pk)
    return render(request, 'resumes/resume_detail.html', {'resume': resume})

class ResumeViewSet(viewsets.ModelViewSet):
    """简历视图集"""
    
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['status', 'job_status']
    search_fields = [
        'name', 'title', 'email', 'phone',
        'job_intention', 'current_location'
    ]
    ordering_fields = ['upload_time', 'name']
    ordering = ['-upload_time']

    def perform_create(self, serializer):
        """创建时自动设置上传者"""
        serializer.save(uploader=self.request.user)

    @action(detail=True, methods=['post'])
    def analyze(self, request, pk=None):
        """触发简历解析"""
        resume = self.get_object()
        
        # 检查是否已经存在解析结果
        if hasattr(resume, 'analysis'):
            return Response(
                {'detail': _('简历已经解析过')},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # TODO: 调用简历解析服务
        # analysis_result = resume_analysis_service.analyze(resume.file.path)
        
        # 创建解析结果（示例数据）
        analysis = ResumeAnalysis.objects.create(
            resume=resume,
            parsed_content={},
            skills=[],
            experience_years=0,
            education_level='未知',
            last_company='未知',
            last_position='未知'
        )
        
        serializer = ResumeAnalysisSerializer(analysis)
        return Response(serializer.data)


class ResumeAnalysisViewSet(viewsets.ReadOnlyModelViewSet):
    """简历解析视图集（只读）"""
    
    queryset = ResumeAnalysis.objects.all()
    serializer_class = ResumeAnalysisSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['education_level']
    search_fields = [
        'resume__name', 'last_company',
        'last_position'
    ]
    ordering_fields = ['analysis_time', 'experience_years']
    ordering = ['-analysis_time']


class ResumeSearchViewSet(viewsets.ReadOnlyModelViewSet):
    """简历检索视图集（只读）"""
    
    queryset = ResumeSearch.objects.all()
    serializer_class = ResumeSearchSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ['query']
    ordering_fields = ['search_time']
    ordering = ['-search_time']

    def get_queryset(self):
        """只返回当前用户的搜索记录"""
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def search(self, request):
        """执行简历搜索"""
        query = request.data.get('keywords', '')
        filters = request.data.get('filters', {})
        
        # TODO: 实现实际的搜索逻辑
        # results = resume_search_service.search(query, filters)
        
        # 记录搜索
        search_record = ResumeSearch.objects.create(
            user=request.user,
            query=query,
            filters=filters,
            results_count=0  # TODO: 设置实际的结果数量
        )
        
        serializer = self.get_serializer(search_record)
        return Response(serializer.data) 