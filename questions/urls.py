from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
]
