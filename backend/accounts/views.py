from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import (
    UserSerializer,
    RegisterSerializer,
)
from .permissions import UserAccountViewPermission
from rest_framework import views, response, status, generics, permissions


# Create your views here.

class AccountView(views.APIView):
    queryset = User.objects.all()
    permission_classes = (UserAccountViewPermission,)

    def get(self, request, **kwargs):
        user = request.user
        serializer = UserSerializer(user, many=False)
        return response.Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class UsernameUserExistsView(views.APIView):
    def get(self, request, username: str, *args, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return response.Response(data={'username': False})
        else:
            return response.Response(data={'username': True})


class EmailUserExistsView(views.APIView):
    def get(self, request, email: str, *args, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return response.Response(data={'email': False})
        else:
            return response.Response(data={'email': True})
