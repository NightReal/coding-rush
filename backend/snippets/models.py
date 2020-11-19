from django.db import models

# Create your models here.

LANGUAGES = ('c++', 'python')
LANGUAGES_CHOICES = [(i, i) for i in LANGUAGES]


class Snippet(models.Model):
    title = models.CharField(max_length=50, blank=True, default='')
    code = models.TextField()
    language = models.CharField(choices=LANGUAGES_CHOICES, max_length=50, default='python')
