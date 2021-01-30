from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, label="ID")

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'language']
