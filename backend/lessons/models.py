from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from .utils.scoring import score

# Create your models here.

LANGUAGES = ('c++', 'python')
LANGUAGES_CHOICES = [(i, i) for i in LANGUAGES]

User = get_user_model()


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, default='', unique=True)
    topic = models.CharField(default='no_topic', blank=False, max_length=50)
    description = models.CharField(default='', max_length=10000)
    difficulty = models.IntegerField(choices=[(i, i) for i in range(1, 11)], default=1)

    def __str__(self):
        return f"{self.id} - {self.title} - {self.topic}"

    class Meta:
        ordering = ['difficulty', 'title']


class Code(models.Model):
    id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='codes')
    language = models.CharField(choices=LANGUAGES_CHOICES, default='python', max_length=10)
    code = models.TextField(blank=True, max_length=10000)

    class Meta:
        unique_together = ['lesson', 'language']
        ordering = ['language']

    def __str__(self):
        return f"{self.lesson}: {self.language}"


class AttemptManager(models.Manager):
    def default_create(self, speed, accuracy, code, *args, **kwargs):
        attempt = self.create(score=score(speed, accuracy, code.lesson.difficulty), speed=speed, accuracy=accuracy, code=code, lesson=code.lesson, *args, **kwargs)

        return attempt


class Attempt(models.Model):
    id = models.AutoField(primary_key=True)
    score = models.BigIntegerField(default=0)
    speed = models.IntegerField(default=0)
    accuracy = models.FloatField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attempts')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='attempts')
    code = models.ForeignKey(Code, on_delete=models.CASCADE, related_name='attempts')
    date = models.DateTimeField(auto_now=True)
    # FIXME: rewrite this to DurationField
    duration = models.IntegerField(default=1)  # duration of attempt in seconds

    objects = AttemptManager()
