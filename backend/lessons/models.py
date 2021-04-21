from django.db import models
from accounts.models import (
    CodingrushAccount,
)
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

LANGUAGES = ('c++', 'python')
LANGUAGES_CHOICES = [(i, i) for i in LANGUAGES]


class Lesson(models.Model):
    title = models.CharField(max_length=50, blank=True, default='')
    topic = models.CharField(default='no_topic', blank=False, max_length=50)
    description = models.CharField(default='', max_length=10000)
    difficulty = models.IntegerField(choices=[(i, i) for i in range(1, 11)], default=1)

    def __str__(self):
        return f"{self.title} - {self.topic}"


class Code(models.Model):
    id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='codes')
    language = models.CharField(choices=LANGUAGES_CHOICES, default='python', max_length=10)
    code = models.CharField(blank=True, max_length=10000)

    class Meta:
        unique_together = ['lesson', 'language']

    def __str__(self):
        return f"{self.lesson} - {self.language}"


class Attempt(models.Model):
    id = models.AutoField(primary_key=True)
    score = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    speed = models.IntegerField(default=0)
    accuracy = models.FloatField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    user = models.ForeignKey(CodingrushAccount, on_delete=models.CASCADE, related_name='attempts')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='attempts')
    code = models.ForeignKey(Code, on_delete=models.CASCADE, related_name='attempts')
