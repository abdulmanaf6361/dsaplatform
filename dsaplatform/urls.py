from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('questions.urls')),
    path('submissions/', include('submissions.urls')),
    path('leaderboard/', include('leaderboard.urls')),
    path('trainer/', include('trainer.urls')),
    path('', include('questions.urls')),
]
