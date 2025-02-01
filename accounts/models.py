from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """自定义用户模型"""
    phone = models.CharField(_('手机号'), max_length=11, blank=True)
    department = models.CharField(_('部门'), max_length=100, blank=True)
    
    class Meta:
        verbose_name = _('用户')
        verbose_name_plural = _('用户') 