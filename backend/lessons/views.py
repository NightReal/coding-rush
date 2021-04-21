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
        serializer = LessonSerializer(lesson)
        return response.Response(serializer.data)


class GetAllLessonsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        user = request.user
        # see above
        # seems like it is NOT optimal here because it executes 1 query of lessons code for each lesson
        # may be it should work with select_related() but I don't understand it quite yet
        prefetch = Prefetch('attempts', queryset=Attempt.objects.filter(user_id=user.id).order_by('lesson_id', '-score').distinct('lesson_id'),
                            to_attr='best_user_attempt')
        lesson = Lesson.objects.prefetch_related(prefetch) .all()
        serializer = LessonListSerializer(lesson, many=True)
        return response.Response(serializer.data)
