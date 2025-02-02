from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Resume(models.Model):
    """简历模型"""
    
    STATUS_CHOICES = [
        ('pending', '待处理'),
        ('parsing', '解析中'),
        ('parsed', '已解析'),
        ('failed', '解析失败'),
    ]

    # 基本信息
    title = models.CharField(_('简历标题'), max_length=200)
    file = models.FileField(_('简历文件'), upload_to='resumes/%Y/%m/')
    file_type = models.CharField(_('文件类型'), max_length=50)
    status = models.CharField(_('状态'), max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # 上传信息
    uploader = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('上传者'),
        related_name='uploaded_resumes'
    )
    upload_time = models.DateTimeField(_('上传时间'), auto_now_add=True)
    
    # 解析后的基本信息
    name = models.CharField(_('姓名'), max_length=50, blank=True)
    email = models.EmailField(_('邮箱'), blank=True)
    phone = models.CharField(_('电话'), max_length=20, blank=True)
    gender = models.CharField(_('性别'), max_length=10, blank=True)
    birth_date = models.DateField(_('出生日期'), null=True, blank=True)
    current_location = models.CharField(_('当前所在地'), max_length=100, blank=True)
    
    # 求职意向
    job_intention = models.CharField(_('求职意向'), max_length=100, blank=True)
    expected_salary = models.CharField(_('期望薪资'), max_length=50, blank=True)
    job_status = models.CharField(_('求职状态'), max_length=50, blank=True)
    
    class Meta:
        verbose_name = _('简历')
        verbose_name_plural = _('简历')
        ordering = ['-upload_time']
        permissions = [
            ("analyze_resume", "Can analyze resume"),
            ("search_resume", "Can search resume"),
        ]

    def __str__(self):
        return f"{self.name or '未知'} - {self.title}"

class Education(models.Model):
    """教育经历"""
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name='educations',
        verbose_name=_('简历')
    )
    school = models.CharField(_('学校'), max_length=100)
    major = models.CharField(_('专业'), max_length=100)
    degree = models.CharField(_('学位'), max_length=50)
    start_date = models.DateField(_('开始时间'))
    end_date = models.DateField(_('结束时间'), null=True, blank=True)
    gpa = models.CharField(_('绩点'), max_length=20, blank=True)
    
    class Meta:
        verbose_name = _('教育经历')
        verbose_name_plural = _('教育经历')
        ordering = ['-end_date']

class WorkExperience(models.Model):
    """工作经历"""
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name='work_experiences',
        verbose_name=_('简历')
    )
    company = models.CharField(_('公司'), max_length=100)
    position = models.CharField(_('职位'), max_length=100)
    start_date = models.DateField(_('开始时间'))
    end_date = models.DateField(_('结束时间'), null=True, blank=True)
    description = models.TextField(_('工作描述'), blank=True)
    
    class Meta:
        verbose_name = _('工作经历')
        verbose_name_plural = _('工作经历')
        ordering = ['-end_date']

class ResumeAnalysis(models.Model):
    """简历解析结果"""
    resume = models.OneToOneField(
        Resume,
        on_delete=models.CASCADE,
        related_name='analysis',
        verbose_name=_('简历')
    )
    parsed_content = models.JSONField(_('解析内容'), default=dict)
    skills = models.JSONField(_('技能标签'), default=list)
    experience_years = models.FloatField(_('工作年限'), null=True, blank=True)
    education_level = models.CharField(_('最高学历'), max_length=50, blank=True)
    last_company = models.CharField(_('最近工作单位'), max_length=100, blank=True)
    last_position = models.CharField(_('最近职位'), max_length=100, blank=True)
    analysis_time = models.DateTimeField(_('解析时间'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('简历解析')
        verbose_name_plural = _('简历解析')

class ResumeSearch(models.Model):
    """简历检索记录"""
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('搜索者'),
        related_name='resume_searches'
    )
    query = models.CharField(
        _('搜索关键词'), 
        max_length=200
    )
    filters = models.JSONField(
        _('搜索条件'), 
        default=dict
    )
    results_count = models.IntegerField(
        _('结果数量'), 
        default=0
    )
    search_time = models.DateTimeField(
        _('搜索时间'), 
        auto_now_add=True
    )
    
    class Meta:
        verbose_name = _('简历检索')
        verbose_name_plural = _('简历检索')
        ordering = ['-search_time'] 