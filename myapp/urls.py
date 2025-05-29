from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('program/', views.program_view, name='program'),
    path('management/', views.ManagementView.as_view(), name='management'),
    path('classmates/', views.ClassmatesView.as_view(), name='classmates'),
    path('students/', views.students_view, name='students'),
]