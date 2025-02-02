from django.db import models
from django.utils.translation import gettext_lazy as _


class Job(models.Model):
    STATUS_CHOICES = [
        ('draft', '草稿'),
        ('published', '已发布'),
        ('closed', '已关闭'),
    ]

    title = models.CharField(_('职位名称'), max_length=100)
    department = models.CharField(_('部门'), max_length=100)
    location = models.CharField(_('工作地点'), max_length=100)
    description = models.TextField(_('职位描述'))
    requirements = models.TextField(_('任职要求'))
    salary_range = models.CharField(_('薪资范围'), max_length=100)
    status = models.CharField(
        _('状态'),
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)

    class Meta:
        verbose_name = _('职位')
        verbose_name_plural = _('职位')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.department}" 