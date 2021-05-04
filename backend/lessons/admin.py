from django.contrib import admin
from .models import (
    Lesson,
    Code,
    Attempt,
)


# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    fields = ['title', 'topic', 'description', 'difficulty']


admin.site.register(Lesson, LessonAdmin)


class CodeAdmin(admin.ModelAdmin):
    fields = ['lesson', 'language', 'code']


admin.site.register(Code, CodeAdmin)


class AttemptAdmin(admin.ModelAdmin):
    fields = ['score', 'speed', 'accuracy', 'user', 'lesson', 'code_language', 'duration']


admin.site.register(Attempt, AttemptAdmin)
