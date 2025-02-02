from django.urls import path
from . import views

app_name = 'resumes'

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('<int:pk>/', views.resume_detail, name='resume_detail'),
] 