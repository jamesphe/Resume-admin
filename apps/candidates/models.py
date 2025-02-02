from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.resumes.models import Resume


class Candidate(models.Model):
    STATUS_CHOICES = [
        ('new', '新候选人'),
        ('screening', '筛选中'),
        ('interviewing', '面试中'),
        ('offered', '已发offer'),
        ('onboard', '已入职'),
        ('rejected', '已拒绝'),
    ]

    resume = models.OneToOneField(
        Resume,
        on_delete=models.CASCADE,
        verbose_name=_('简历')
    )
    status = models.CharField(
        _('状态'),
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )
    notes = models.TextField(_('备注'), blank=True)
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)

    class Meta:
        verbose_name = _('候选人')
        verbose_name_plural = _('候选人')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.resume.name} - {self.get_status_display()}" 