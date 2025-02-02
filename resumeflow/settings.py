from pathlib import Path
import os
import environ

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
    # 自定义应用
    'accounts.apps.AccountsConfig',
    'resumes.apps.ResumesConfig',
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
    "site_brand": "ATS Admin",
    
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

    # 更新图标设置
    "icons": {
        # 简历管理
        "resumes": "fas fa-folder",  # 简历管理模块
        "resumes.Resume": "fas fa-file-alt",  # 简历
        "resumes.ResumeAnalysis": "fas fa-chart-line",  # 简历分析
        "resumes.ResumeReport": "fas fa-file-contract",  # 分析报告

        # 简历筛查
        "screening": "fas fa-filter",  # 筛查管理模块
        "screening.Position": "fas fa-bullseye",  # 职位
        "screening.ScreeningTask": "fas fa-tasks",  # 筛查任务
        "screening.JobDescription": "fas fa-clipboard-list",  # 职位描述
        "screening.Requirement": "fas fa-list-check",  # 要求
        "screening.Evaluation": "fas fa-star",  # 评估

        # 向量检索
        "vector_search": "fas fa-search",  # 向量检索模块
        "vector_search.SearchLog": "fas fa-history",  # 搜索日志
        "vector_search.VectorIndex": "fas fa-database",  # 向量索引

        # 语言模型
        "language_models": "fas fa-robot",  # 语言模型模块
        "language_models.Model": "fas fa-brain",  # 模型
        "language_models.ModelConfig": "fas fa-cog",  # 模型配置

        # 用户权限
        "auth": "fas fa-shield-alt",  # 权限模块
        "auth.user": "fas fa-user",  # 用户
        "auth.Group": "fas fa-users",  # 用户组
        "accounts.User": "fas fa-user-tie",  # 账户

        # 其他图标
        "sites": "fas fa-globe",
        "admin": "fas fa-cog",
    },

    # 菜单标签
    "menu_labels": {
        "resumes": "简历管理",
        "screening": "简历筛查",
        "vector_search": "向量检索",
        "language_models": "语言模型",
        "auth": "用户权限",
        "accounts": "账户管理",
    },

    # 自定义菜单
    "custom_links": {
        "resumes": [{
            "name": "简历分析",
            "url": "admin:resumes_resume_changelist",
            "icon": "fas fa-chart-bar",
        }],
        "screening": [{
            "name": "筛查任务",
            "url": "admin:screening_screeningtask_changelist",
            "icon": "fas fa-tasks",
        }],
        "vector_search": [{
            "name": "搜索记录",
            "url": "admin:vector_search_searchlog_changelist",
            "icon": "fas fa-history",
        }],
    },

    # 菜单显示设置
    "show_sidebar": True,
    "navigation_expanded": True,
    
    # 菜单顺序
    "order_with_respect_to": [
        "auth",
        "accounts",
        "resumes",
        "screening",
        "vector_search",
        "language_models",
    ],

    # 自定义CSS
    "custom_css": "css/custom_admin.css",
    
    # 界面设置
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    
    # 顶部导航
    "topmenu_links": [
        {"name": "首页", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "简历管理", "url": "admin:resumes_resume_changelist", "permissions": ["resumes.view_resume"]},
        {"model": "auth.User"},
        {"app": "resumes"},
    ],
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