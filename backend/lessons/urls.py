from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    GetLessonView,
    GetAllLessonsView,
    CommitAttemptView,
)

urlpatterns = [
    path('<int:pk>/', GetLessonView.as_view(), name='Get lesson'),
    path('', GetAllLessonsView.as_view(), name='Get all lessons'),
    path('commitAttempt/', CommitAttemptView.as_view(), name='Commit new attempt')
]

urlpatterns = format_suffix_patterns(urlpatterns)
