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
    fields = ['score', 'speed', 'accuracy', 'user', 'code', 'duration']

    def save_model(self, request, obj, form, change):
        obj.lesson = obj.code.lesson
        super().save_model(request, obj, form, change)


admin.site.register(Attempt, AttemptAdmin)
