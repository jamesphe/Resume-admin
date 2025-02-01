INSTALLED_APPS = [
    'jazzmin',  # 必须放在 django.contrib.admin 之前
    'django.contrib.admin',
    # ... 其他应用
]

# Jazzmin 配置
JAZZMIN_SETTINGS = {
    # 网站标题
    "site_title": "智能简历筛查系统",
    "site_header": "智能简历筛查系统",
    "site_brand": "ATS Admin",
    
    # 主题配色
    "theme": "default",
    "dark_mode_theme": "darkly",
    
    # 顶部导航
    "topmenu_links": [
        {"name": "首页", "url": "admin:index"},
        {"name": "简历管理", "url": "admin:resumes_resume_changelist"},
    ],
    
    # 侧边栏设置
    "navigation_expanded": True,
    
    # UI 定制
    "show_ui_builder": True,
    
    # 自定义样式
    "custom_css": None,
    "custom_js": None,
    
    # 图标设置
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "resumes.Resume": "fas fa-file-alt",
    },
    
    # 版权信息
    "copyright": "智能简历筛查系统 版权所有",
    
    # 欢迎文本
    "welcome_sign": "欢迎使用简历筛查系统",
    
    # 登录界面设置
    "login_logo": None,
    "login_logo_dark": None,
    "show_sidebar": True,
    "navigation_expanded": True,
    
    # 用户头像
    "user_avatar": None,
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