from django.db import models
from django.utils.translation import gettext_lazy as _

class Resume(models.Model):
    EDUCATION_CHOICES = [
        ('high_school', '高中'),
        ('college', '大专'),
        ('bachelor', '本科'),
        ('master', '硕士'),
        ('phd', '博士'),
    ]

    name = models.CharField(_('姓名'), max_length=100)
    phone = models.CharField(_('电话'), max_length=20)
    email = models.EmailField(_('邮箱'))
    education = models.CharField(_('学历'), max_length=20, choices=EDUCATION_CHOICES)
    school = models.CharField(_('学校'), max_length=100)
    major = models.CharField(_('专业'), max_length=100)
    work_experience = models.TextField(_('工作经验'))
    skills = models.TextField(_('技能'))
    file = models.FileField(_('简历文件'), upload_to='resumes/')
    vector_id = models.CharField(_('向量ID'), max_length=100, blank=True)
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)

    class Meta:
        verbose_name = _('简历')
        verbose_name_plural = _('简历')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.education}" 