from django.apps import AppConfig

class VectorSearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vector_search'
    verbose_name = '向量检索' 