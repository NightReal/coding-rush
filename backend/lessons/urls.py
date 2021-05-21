from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    GetLessonView,
    GetAllLessonsView,
    CommitAttemptView,
    UserStatisticsGetView,
)

urlpatterns = [
    path('<int:pk>', GetLessonView.as_view(), name='Get lesson'),
    path('', GetAllLessonsView.as_view(), name='Get all lessons'),
    path('commitAttempt', CommitAttemptView.as_view(), name='Commit new attempt'),
    path('attempts/<str:username>', UserStatisticsGetView.as_view(), name='Get user statistics data'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
