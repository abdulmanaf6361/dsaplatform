from django.urls import path
from . import views

urlpatterns = [
    path('run/<int:question_id>/', views.run_code, name='run_code'),
    path('submit/<int:question_id>/', views.submit_code, name='submit_code'),
    path('result/<int:submission_id>/', views.submission_result, name='submission_result'),
    path('history/<int:question_id>/', views.my_submissions, name='my_submissions'),
]
