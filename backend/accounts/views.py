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
