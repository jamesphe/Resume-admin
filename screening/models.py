from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class JobDescription(models.Model):
    """职位描述"""
    title = models.CharField(_('职位名称'), max_length=100)
    description = models.TextField(_('职位描述'))
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('创建者')
    )
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    vector_embedding = models.BinaryField(_('向量表示'), null=True)
    
    class Meta:
        verbose_name = _('职位描述')
        verbose_name_plural = _('职位描述')

class ScreeningTask(models.Model):
    """筛查任务"""
    STATUS_CHOICES = [
        ('pending', '待处理'),
        ('processing', '处理中'),
        ('completed', '已完成'),
        ('failed', '失败'),
    ]

    job = models.ForeignKey(
        JobDescription,
        on_delete=models.CASCADE,
        verbose_name=_('职位')
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('创建者')
    )
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    status = models.CharField(
        _('状态'),
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    result = models.JSONField(_('筛查结果'), null=True, blank=True)
    
    class Meta:
        verbose_name = _('筛查任务')
        verbose_name_plural = _('筛查任务') 