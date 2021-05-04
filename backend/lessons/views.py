from rest_framework import (
    generics,
    permissions,
    response,
    status,
    views,
)
from .serializers import (
    LessonSerializer,
    LessonListSerializer,
)
from .models import (
    Lesson,
    Attempt,
)
from django.db.models import (
    Prefetch,
    Max,
)


# Create your views here.

class GetLessonView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, pk: int, *args, **kwargs):
        user = request.user
        lesson = Lesson.objects.filter(id=pk).first()
        if lesson is None:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        lesson.cur_user_attempts = Attempt.objects.filter(user_id=user.id, lesson_id=pk).order_by('-id')
        serializer = LessonSerializer(lesson, read_only=True)
        return response.Response(serializer.data)


class GetAllLessonsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        user = request.user
        prefetch = Prefetch('attempts', queryset=Attempt.objects.filter(user_id=user.id).order_by('-score', '-id'))
        lessons = Lesson.objects.prefetch_related(prefetch).prefetch_related('codes')
        for lesson in lessons:
            best = lesson.attempts.first()
            if best:
                lesson.best_user_attempt = best
        serializer = LessonListSerializer(lessons, many=True, read_only=True)
        return response.Response(serializer.data)
