from django.contrib.auth import get_user_model

from .serializers import (
    ChangePasswordSerializer,
    UserRegisterSerializer,
    PrivateProfileInformationSerializer,
    ProfileUpdateSerializer,
    PublicProfileInformationSerializer,
)
from rest_framework.response import (
    Response,
)
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)
from rest_framework import (
    views,
    permissions,
    generics,
)

User = get_user_model()


# Create your views here.

class UserRegisterView(generics.CreateAPIView):
    """
    User registration endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny, ]


class ChangePasswordView(views.APIView):
    """
    Password change endpoint
    """
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.update()
            return Response(status=HTTP_204_NO_CONTENT)

        return Response(status=HTTP_400_BAD_REQUEST)


class UsernameUserExistsView(views.APIView):
    """
    Check if user with such username exists
    """
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, username: str, *args, **kwargs):
        user = User.objects.filter(username__iexact=username)
        res = {'username': bool(user)}
        return Response(res)


class EmailUserExistsView(views.APIView):
    """
    Check in user with such email exists
    """
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, email: str, *args, **kwargs):
        user = User.objects.filter(email=email)
        res = {'email': bool(user)}
        return Response(res)


class PrivateUserProfileView(views.APIView):
    """
    Private profile information retrieve
    """
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, **kwargs):
        user = request.user
        serializer = PrivateProfileInformationSerializer(user)
        data = serializer.data
        return Response(data)


class PublicProfileInformationView(views.APIView):
    """
    Public profile information retrieve
    """
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, username: str, *args, **kwargs):
        user = User.objects.filter(username__iexact=username).first()
        if user is None:
            return Response(status=HTTP_404_NOT_FOUND)
        serializer = PublicProfileInformationSerializer(user)
        data = serializer.data
        return Response(data)


class ProfileUpdateView(views.APIView):
    """
    Endpoint for changing profile information
    """
    serializer_class = ProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            user = request.user
            serializer.update(user, serializer.validated_data)
            return Response(status=HTTP_204_NO_CONTENT)

        return Response(status=HTTP_400_BAD_REQUEST)
