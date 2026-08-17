from django.urls import path
from . import views

urlpatterns = [
    path('', views.practice_dashboard, name='practice_dashboard'),
    path('question/<int:question_id>/', views.practice_question, name='practice_question'),
    path('run/<int:question_id>/', views.practice_run, name='practice_run'),
    path('submit/<int:question_id>/', views.practice_submit, name='practice_submit'),
    path('result/<int:submission_id>/', views.practice_result, name='practice_result'),
    path('history/<int:question_id>/', views.practice_my_submissions, name='practice_my_submissions'),
    # Trainer
    path('trainer/', views.trainer_practice_dashboard, name='trainer_practice_dashboard'),
    path('trainer/day/<int:day_id>/toggle/<int:batch_id>/', views.trainer_toggle_practice_day, name='trainer_toggle_practice_day'),
    path('trainer/submissions/', views.trainer_practice_submissions, name='trainer_practice_submissions'),
    path('trainer/submissions/<int:submission_id>/', views.trainer_practice_submission_detail, name='trainer_practice_submission_detail'),
    path('trainer/progress/', views.trainer_practice_progress, name='trainer_practice_progress'),
]
