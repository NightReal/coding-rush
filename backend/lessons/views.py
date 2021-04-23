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
        # IDK, maybe this is slow, but I didn't found better solution. See LessonSerializer for better understanding of this hack.
        # Seems like that currently it executes 3 SQL queries and it is the fastest possible result with current models
        prefetch = Prefetch('attempts', queryset=Attempt.objects.filter(user_id=user.id), to_attr='cur_user_attempts')
        # don't use get() here because it throws exception when there is no lesson with such id
        lesson = Lesson.objects.prefetch_related(prefetch).filter(id=pk).first()
        if lesson is None:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LessonSerializer(lesson, read_only=True)
        return response.Response(serializer.data)


class GetAllLessonsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        user = request.user
        # see above
        # FIXME: rewrite this bullshit.
        # to_attr is simply a list, and used as source in serializer.
        # means that we can just do some magic and put best_user_attempt quicker than here and without postprocessing to single-model
        prefetch = Prefetch('attempts', queryset=Attempt.objects.filter(user_id=user.id).order_by('lesson_id', '-score').distinct('lesson_id'),
                            to_attr='best_user_attempt')
        lessons = Lesson.objects.prefetch_related(prefetch).prefetch_related('codes').all()
        for lesson in lessons:
            if len(lesson.best_user_attempt):
                lesson.best_user_attempt = lesson.best_user_attempt[0]
            else:
                del lesson.best_user_attempt
        serializer = LessonListSerializer(lessons, many=True, read_only=True)
        return response.Response(serializer.data)
