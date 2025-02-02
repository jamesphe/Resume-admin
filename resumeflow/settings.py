from pathlib import Path
import os
import environ
from django.urls import path, include

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 初始化环境变量
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-your-secret-key-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'jazzmin',  # 必须是第一个
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 第三方应用
    'rest_framework',
    'django_filters',
    # 自定义应用
    'accounts.apps.AccountsConfig',
    'resumes.apps.ResumesConfig',
    'candidates.apps.CandidatesConfig',  
    'positions.apps.PositionsConfig',    
    'interviews.apps.InterviewsConfig',  
    'analytics.apps.AnalyticsConfig',    
    'screening.apps.ScreeningConfig',
    'language_models.apps.LanguageModelsConfig',
    'vector_search.apps.VectorSearchConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'resumeflow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'resumeflow.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 自定义用户模型
AUTH_USER_MODEL = 'accounts.User'

# Internationalization
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 确保在开发环境中添加以下配置
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 登录配置
LOGIN_URL = 'admin:login'
LOGIN_REDIRECT_URL = 'admin:index'
LOGOUT_URL = 'admin:logout'

# 文件上传配置
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]
MAX_UPLOAD_SIZE = 5242880  # 5MB

# Jazzmin 配置
JAZZMIN_SETTINGS = {
    # 网站标题
    "site_title": "智能简历筛查系统",
    "site_header": "智能简历筛查系统",
    "site_brand": "智能简历筛查系统",
    
    # 登录界面设置
    "login_logo": None,  # 可以添加登录页面的 logo
    "login_logo_dark": None,  # 深色主题的 logo
    "site_logo": None,  # 网站 logo
    "welcome_sign": "欢迎使用简历筛查系统",  # 登录页面的欢迎文本
    "copyright": "智能简历筛查系统 版权所有",  # 版权信息
    "search_model": ["auth.User", "resumes.Resume"],  # 搜索模型
    
    # 登录界面的背景色和样式
    "login_ui_tweaks": {
        "navbar_small_text": False,
        "footer_small_text": False,
        "body_small_text": False,
        "brand_small_text": False,
        "brand_colour": False,
        "accent": "accent-primary",
        "navbar": "navbar-dark",
        "no_navbar_border": False,
        "navbar_fixed": False,
        "layout_boxed": False,
        "footer_fixed": False,
        "sidebar_fixed": False,
        "sidebar": "sidebar-dark-primary",
        "sidebar_nav_small_text": False,
        "sidebar_disable_expand": False,
        "sidebar_nav_child_indent": False,
        "sidebar_nav_compact_style": False,
        "sidebar_nav_legacy_style": False,
        "sidebar_nav_flat_style": False,
    },

    # 重新定义菜单结构，严格按照系统设计文档
    "menu": [
        # 首页
        {
            "name": "首页",
            "url": "admin:index", 
            "icon": "fas fa-home"
        },
        
        # 简历管理
        {
            "name": "简历管理",
            "icon": "fas fa-file-alt",
            "permissions": ["resumes.view_resume"],  # 添加权限控制
            "children": [
                {
                    "name": "简历上传",
                    "model": "resumes.resume",  # 使用 model 而不是 url
                    "icon": "fas fa-upload"
                },
                {
                    "name": "简历解析",
                    "model": "resumes.resumeanalysis",
                    "icon": "fas fa-search"
                },
                {
                    "name": "简历存储",
                    "model": "resumes.resume",
                    "icon": "fas fa-database"
                },
                {
                    "name": "简历检索",
                    "model": "resumes.resumesearch",
                    "icon": "fas fa-search"
                }
            ]
        },
        
        # 候选人管理
        {
            "name": "候选人管理",
            "icon": "fas fa-users",
            "children": [
                {
                    "name": "候选人档案",
                    "url": "admin:candidates_candidate_changelist",
                    "icon": "fas fa-address-card"
                },
                {
                    "name": "候选人评估",
                    "url": "admin:candidates_evaluation_changelist",
                    "icon": "fas fa-star"
                },
                {
                    "name": "候选人推荐",
                    "url": "admin:candidates_recommendation_changelist",
                    "icon": "fas fa-user-check"
                }
            ]
        },
        
        # 职位管理
        {
            "name": "职位管理",
            "icon": "fas fa-briefcase",
            "children": [
                {
                    "name": "职位发布",
                    "url": "admin:positions_position_add",
                    "icon": "fas fa-plus"
                },
                {
                    "name": "职位维护",
                    "url": "admin:positions_position_changelist",
                    "icon": "fas fa-cog"
                }
            ]
        },
        
        # 面试管理
        {
            "name": "面试管理",
            "icon": "fas fa-comments",
            "children": [
                {
                    "name": "面试安排",
                    "url": "admin:interviews_interview_add",
                    "icon": "fas fa-calendar-plus"
                },
                {
                    "name": "面试记录",
                    "url": "admin:interviews_interview_changelist",
                    "icon": "fas fa-clipboard-list"
                }
            ]
        },
        
        # 招聘分析
        {
            "name": "招聘分析",
            "icon": "fas fa-chart-line",
            "children": [
                {
                    "name": "招聘进度",
                    "url": "admin:analytics_recruitmentprogress_changelist",
                    "icon": "fas fa-tasks"
                },
                {
                    "name": "招聘效果",
                    "url": "admin:analytics_recruitmentmetrics_changelist",
                    "icon": "fas fa-chart-bar"
                }
            ]
        },
        
        # 系统设置（原系统管理）
        {
            "name": "系统设置",
            "icon": "fas fa-cogs",
            "permissions": ["auth.view_user"],  # 确保有权限的用户才能看到
            "children": [
                {
                    "name": "用户管理",
                    "url": "admin:auth_user_changelist",
                    "icon": "fas fa-user"
                },
                {
                    "name": "角色管理",
                    "url": "admin:auth_group_changelist",
                    "icon": "fas fa-users"
                },
                {
                    "name": "权限管理",
                    "url": "admin:auth_permission_changelist",
                    "icon": "fas fa-key"
                }
            ]
        }
    ],

    # 添加应用图标
    "icons": {
        "resumes.Resume": "fas fa-file",
        "resumes.ResumeAnalysis": "fas fa-search",
        "resumes.ResumeSearch": "fas fa-database",
    },
    
    # 确保使用自定义菜单
    "use_custom_menu": True,
    "show_sidebar": True,
    "navigation_expanded": True,
    
    # 禁用默认菜单
    "show_ui_builder": False,
}

# UI相关配置
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

# 修改 Debug Toolbar 配置
if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
    
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    
    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE  # 确保 debug_toolbar 中间件在最前面
    
    INTERNAL_IPS = [
        '127.0.0.1',
    ]
    
    # Debug Toolbar 配置
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: True,
    }

# 添加 REST Framework 配置
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
} 