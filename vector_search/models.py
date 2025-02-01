from django.db import models
from django.utils.translation import gettext_lazy as _

class SearchLog(models.Model):
    """搜索日志"""
    query = models.TextField(_('搜索内容'))
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('搜索日志')
        verbose_name_plural = _('搜索日志') 