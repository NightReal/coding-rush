from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    SlugRelatedField,
    PrimaryKeyRelatedField,
    IntegerField,
)
from .models import (
    Code,
    Lesson,
    Attempt,
)


class AttemptSerializer(ModelSerializer):
    code = SlugRelatedField(read_only=True, slug_field='language')

    class Meta:
        model = Attempt
        fields = ('id', 'score', 'speed', 'accuracy', 'code', 'date', 'duration')
        read_only_fields = fields


# FIXME: MAKE NORMAL VALIDATORS. OTHERWISE IT CAN BREAK THE SYSTEM
class AttemptCommitSerializer(ModelSerializer):
    code = PrimaryKeyRelatedField(queryset=Code.objects.all())

    class Meta:
        model = Attempt
        fields = ('speed', 'accuracy', 'code', 'duration')

    def create(self, validated_data):
        return Attempt.objects.default_create(**self.context, **validated_data)


class CodeSerializer(ModelSerializer):
    class Meta:
        model = Code
        fields = ('id', 'language', 'code')
        read_only_fields = fields


class LessonSerializer(ModelSerializer):
    codes = CodeSerializer(many=True, read_only=True)
    attempts = AttemptSerializer(many=True, read_only=True, source='cur_user_attempts')
    next_lesson = PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'topic', 'description', 'difficulty', 'codes', 'attempts', 'next_lesson')
        read_only_fields = fields


class LessonListSerializer(ModelSerializer):
    codes = SlugRelatedField(many=True, read_only=True, slug_field='language')
    best_attempt = AttemptSerializer(many=False, read_only=True, source='best_user_attempt', required=False)

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'topic', 'difficulty', 'codes', 'best_attempt')
        read_only_fields = fields


class LessonStatisticsSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'topic', 'difficulty')


class AttemptStatisticsSerializer(ModelSerializer):
    code_language = SlugRelatedField(read_only=True, slug_field='language', source='code')
    lesson = LessonStatisticsSerializer(many=False, read_only=True)

    class Meta:
        model = Attempt
        fields = ('score', 'speed', 'accuracy', 'code_language', 'date', 'lesson')
