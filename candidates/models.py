from django.db import models
from django.utils.translation import gettext_lazy as _

class Candidate(models.Model):
    """候选人模型"""
    name = models.CharField(_('姓名'), max_length=100)
    phone = models.CharField(_('电话'), max_length=20)
    email = models.EmailField(_('邮箱'))
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('候选人')
        verbose_name_plural = _('候选人')
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Evaluation(models.Model):
    """候选人评估记录"""
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        verbose_name=_('候选人')
    )
    score = models.IntegerField(_('评分'))
    comments = models.TextField(_('评语'))
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('评估记录')
        verbose_name_plural = _('评估记录')
        ordering = ['-created_at'] 