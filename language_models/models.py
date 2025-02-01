from django.db import models
from django.utils.translation import gettext_lazy as _

class LanguageModel(models.Model):
    """语言模型配置"""
    MODEL_TYPES = [
        ('zhipu', '智谱AI'),
        ('deepseek', 'Deepseek'),
        ('qianwen', '通义千问'),
    ]

    name = models.CharField(_('模型名称'), max_length=100)
    model_type = models.CharField(
        _('模型类型'),
        max_length=20,
        choices=MODEL_TYPES
    )
    api_url = models.URLField(_('API地址'))
    api_key = models.CharField(_('API密钥'), max_length=200)
    is_active = models.BooleanField(_('是否启用'), default=True)
    
    # 模型参数
    temperature = models.FloatField(_('温度'), default=0.7)
    max_tokens = models.IntegerField(_('最大token数'), default=2000)
    config = models.JSONField(_('其他配置'), default=dict, blank=True)
    
    class Meta:
        verbose_name = _('语言模型')
        verbose_name_plural = _('语言模型')

    def __str__(self):
        return f"{self.get_model_type_display()} - {self.name}" 