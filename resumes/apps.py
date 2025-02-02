from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ResumesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'resumes'
    verbose_name = _('简历管理')
    
    def ready(self):
        try:
            import resumes.signals  # noqa F401
        except ImportError:
            pass 