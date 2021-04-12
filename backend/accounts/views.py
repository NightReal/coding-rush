from django.contrib.auth import get_user_model

from .serializers import (
    ChangePasswordSerializer,
    UserRegisterSerializer,
    PrivateProfileInformationSerializer,
)
from rest_framework import (
    views,
    response,
    permissions,
    generics,
)

User = get_user_model()


# Create your views here.

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny, ]


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class UsernameUserExistsView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, username: str, *args, **kwargs):
        user = User.objects.filter(username__iexact=username)
        res = {'username': bool(user)}
        return response.Response(res)


class EmailUserExistsView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, email: str, *args, **kwargs):
        user = User.objects.filter(email=email)
        res = {'email': bool(user)}
        return response.Response(res)


class PrivateUserProfileView(views.APIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, **kwargs):
        user = request.user
        serializer = PrivateProfileInformationSerializer(user)
        data = serializer.data
        return response.Response(data)
