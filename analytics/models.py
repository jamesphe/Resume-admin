from django.db import models
from django.utils.translation import gettext_lazy as _
from positions.models import Position


class RecruitmentProgress(models.Model):
    """招聘进度分析"""
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name=_('职位')
    )
    total_candidates = models.IntegerField(_('候选人数量'))
    interviewed = models.IntegerField(_('已面试人数'))
    passed = models.IntegerField(_('通过人数'))
    report_date = models.DateField(_('统计日期'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('招聘进度')
        verbose_name_plural = _('招聘进度')
        ordering = ['-report_date']
        get_latest_by = 'report_date'

    def __str__(self):
        return f"{self.position} - {self.report_date}"


class RecruitmentEffectiveness(models.Model):
    """招聘效果分析"""
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name=_('职位')
    )
    time_to_fill = models.IntegerField(
        _('职位填充时间(天)'),
        help_text=_('从职位发布到成功招聘的天数')
    )
    cost_per_hire = models.DecimalField(
        _('招聘成本'),
        max_digits=10,
        decimal_places=2,
        help_text=_('每个职位的平均招聘成本')
    )
    source_effectiveness = models.JSONField(
        _('招聘渠道效果'),
        help_text=_('各招聘渠道的效果数据')
    )
    report_date = models.DateField(_('统计日期'), auto_now_add=True)

    class Meta:
        verbose_name = _('招聘效果')
        verbose_name_plural = _('招聘效果')
        ordering = ['-report_date']
        get_latest_by = 'report_date'

    def __str__(self):
        return f"{self.position} - {self.report_date}" 