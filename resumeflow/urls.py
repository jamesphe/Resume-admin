from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# 基本 URL 配置
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('resumes/', include('resumes.urls')),
    path('candidates/', include('candidates.urls')),
    path('positions/', include('positions.urls')),
    path('interviews/', include('interviews.urls')),
    path('analytics/', include('analytics.urls')),
    path('', RedirectView.as_view(
        url='admin/', 
        permanent=False
    )),
]

# 添加静态和媒体文件的 URL
urlpatterns += static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT
)
urlpatterns += static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
)

# Debug Toolbar URL 配置
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns 