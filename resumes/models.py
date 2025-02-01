from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Resume(models.Model):
    """简历模型"""
    STATUS_CHOICES = [
        ('pending', '待处理'),
        ('processing', '处理中'),
        ('completed', '已完成'),
        ('failed', '处理失败'),
    ]

    title = models.CharField(_('简历标题'), max_length=200)
    file = models.FileField(_('简历文件'), upload_to='resumes/%Y/%m/')
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('上传者')
    )
    uploaded_at = models.DateTimeField(_('上传时间'), auto_now_add=True)
    status = models.CharField(
        _('处理状态'),
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    
    # 结构化数据
    parsed_data = models.JSONField(_('解析数据'), null=True, blank=True)
    
    class Meta:
        verbose_name = _('简历')
        verbose_name_plural = _('简历')
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title

class ResumeAnalysis(models.Model):
    """简历AI分析报告"""
    resume = models.OneToOneField(
        Resume,
        on_delete=models.CASCADE,
        related_name='analysis',
        verbose_name=_('简历')
    )
    analysis_text = models.TextField(_('分析内容'))
    created_at = models.DateTimeField(_('生成时间'), auto_now_add=True)
    vector_embedding = models.BinaryField(_('向量表示'), null=True)
    
    class Meta:
        verbose_name = _('简历分析')
        verbose_name_plural = _('简历分析') 