from django.shortcuts import render
from .models import Snippet
from .serializers import SnippetSerializer
from django.http import Http404
from rest_framework import generics


# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets, or create new one
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveAPIView):
    """
    Retrieve snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
