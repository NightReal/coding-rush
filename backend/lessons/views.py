from rest_framework import generics, permissions
from .serializers import (
    LessonSerializer,
    LessonListSerializer,
)
from .models import (
    Lesson,
)


# Create your views here.

class GetLessonView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.AllowAny, ]


class GetAllLessonsView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer
    permission_classes = [permissions.AllowAny, ]
