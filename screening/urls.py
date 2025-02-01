from django.urls import path
from . import views

app_name = 'screening'

urlpatterns = [
    path('', views.screening_view, name='screen'),
] 