from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics, permissions


# Create your views here.

class SnippetList(generics.ListAPIView):
    """
    List all snippets
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetCreate(generics.CreateAPIView):
    """
    Create snippet
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveAPIView):
    """
    Retrieve snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
