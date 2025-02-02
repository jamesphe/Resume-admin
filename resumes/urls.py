from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# 创建路由器
router = DefaultRouter()
router.register(r'resumes', views.ResumeViewSet)
router.register(r'analyses', views.ResumeAnalysisViewSet)
router.register(r'searches', views.ResumeSearchViewSet)

app_name = 'resumes'

urlpatterns = [
    path('', include(router.urls)),
] 