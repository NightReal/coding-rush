from rest_framework.response import (
    Response,
)
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)
from rest_framework import (
    permissions,
    views,
)
from .serializers import (
    LessonSerializer,
    LessonListSerializer,
    AttemptCommitSerializer,
    AttemptSerializer,
    AttemptStatisticsSerializer,
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
        lesson = Lesson.objects.filter(id=pk).first()
        if lesson is None:
            return Response(status=HTTP_404_NOT_FOUND)
        next_lesson = Lesson.objects.filter(id__gt=lesson.id).order_by("id").first()
        if next_lesson:
            lesson.next_lesson = next_lesson
        lesson.cur_user_attempts = Attempt.objects.filter(user_id=user.id, lesson_id=pk).order_by('-id')
        serializer = LessonSerializer(lesson, read_only=True)
        return Response(serializer.data)


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
        return Response(serializer.data)


class CommitAttemptView(views.APIView):
    serializer_class = AttemptCommitSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def put(self, request, *args, **kwargs):
        commit_serializer = self.serializer_class(data=request.data, context={'user': request.user})
        if commit_serializer.is_valid(raise_exception=True):
            attempt = commit_serializer.save()
            ret_serializer = AttemptSerializer(attempt)
            return Response(status=HTTP_200_OK, data=ret_serializer.data)
        return Response(status=HTTP_400_BAD_REQUEST)


class UserStatisticsGetView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, user_id, *args, **kwargs):
        all_attempts = Attempt.objects.filter(user_id=user_id).all()
        lessons_cnt = Lesson.objects.count()
        serializer = AttemptStatisticsSerializer(all_attempts, many=True, read_only=True)
        ret = {
            "lessons_count": lessons_cnt,
            "attempts": serializer.data,
        }
        return Response(ret)
