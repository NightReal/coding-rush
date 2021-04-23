from rest_framework import serializers
from .models import (
    Code,
    Lesson,
    Attempt,
)


class AttemptSerializer(serializers.ModelSerializer):
    # TODO: validator for code_language existence for future write-ability
    class Meta:
        model = Attempt
        fields = ('id', 'score', 'speed', 'accuracy', 'code_language')
        read_only_fields = fields


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ('language', 'code')
        read_only_fields = fields


class LessonSerializer(serializers.ModelSerializer):
    codes = CodeSerializer(many=True, read_only=True)
    attempts = AttemptSerializer(many=True, read_only=True, source='cur_user_attempts')

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'topic', 'description', 'difficulty', 'codes', 'attempts')
        read_only_fields = fields


class LessonListSerializer(serializers.ModelSerializer):
    codes = serializers.SlugRelatedField(many=True, read_only=True, slug_field='language')
    best_attempt = AttemptSerializer(many=False, read_only=True, source='best_user_attempt', required=False)

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'topic', 'difficulty', 'codes', 'best_attempt')
        read_only_fields = fields
