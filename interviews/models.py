from django.db import models
from django.utils.translation import gettext_lazy as _
from candidates.models import Candidate
from positions.models import Position


class Interview(models.Model):
    """面试模型"""
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        verbose_name=_('候选人')
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name=_('应聘职位')
    )
    interview_time = models.DateTimeField(_('面试时间'))
    interview_type = models.CharField(
        _('面试类型'),
        max_length=20,
        choices=[
            ('phone', '电话面试'),
            ('video', '视频面试'),
            ('onsite', '现场面试'),
        ]
    )
    status = models.CharField(
        _('状态'),
        max_length=20,
        choices=[
            ('scheduled', '已安排'),
            ('completed', '已完成'),
            ('cancelled', '已取消'),
        ],
        default='scheduled'
    )
    feedback = models.TextField(_('面试反馈'), blank=True)
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)

    class Meta:
        verbose_name = _('面试')
        verbose_name_plural = _('面试')
        ordering = ['-interview_time']

    def __str__(self):
        return f"{self.candidate} - {self.position} - {self.get_interview_type_display()}" 