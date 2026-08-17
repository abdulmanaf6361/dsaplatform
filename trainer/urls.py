from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainer_dashboard, name='trainer_dashboard'),
    path('day/<int:day_id>/toggle/<int:batch_id>/', views.toggle_day, name='toggle_day'),
    path('submissions/', views.view_submissions, name='trainer_submissions'),
    path('submissions/<int:submission_id>/', views.view_submission_detail, name='trainer_submission_detail'),
    path('progress/', views.student_progress, name='student_progress'),
]
