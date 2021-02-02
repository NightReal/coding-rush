from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from .serializers import (
    PrivateUserSerializer,
    RegisterSerializer,
    PublicUserSerializer,
)
from rest_framework import (
    views,
    response,
    generics,
    permissions
)


# Create your views here.

class PrivateAccountView(views.APIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, **kwargs):
        user = request.user
        serializer = PrivateUserSerializer(user, many=False)
        return response.Response(serializer.data)


class PublicAccountView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()

    def get(self, request, username, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        serializer = PublicUserSerializer(user, many=False)
        return response.Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class UsernameUserExistsView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, username: str, *args, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return response.Response(data={'username': False})
        else:
            return response.Response(data={'username': True})


class EmailUserExistsView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, email: str, *args, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return response.Response(data={'email': False})
        else:
            return response.Response(data={'email': True})
