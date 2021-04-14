from django.contrib.auth import get_user_model

from .serializers import (
    ChangePasswordSerializer,
    UserRegisterSerializer,
    PrivateProfileInformationSerializer,
    ProfileUpdateSerializer,
    PublicProfileInformationSerializer,
)
from rest_framework import (
    views,
    response,
    permissions,
    generics,
    status,
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

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.update()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

        return response.Response(status=status.HTTP_400_BAD_REQUEST)


class UsernameUserExistsView(views.APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, username: str, *args, **kwargs):
        user = User.objects.filter(username__iexact=username)
        res = {'username': bool(user)}
        return response.Response(res)


class EmailUserExistsView(views.APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, email: str, *args, **kwargs):
        user = User.objects.filter(email=email)
        res = {'email': bool(user)}
        return response.Response(res)


class PrivateUserProfileView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, **kwargs):
        user = request.user
        serializer = PrivateProfileInformationSerializer(user)
        data = serializer.data
        return response.Response(data)


class PublicProfileInformationView(views.APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, username: str, *args, **kwargs):
        user = User.objects.filter(username__iexact=username).first()
        if user is None:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PublicProfileInformationSerializer(user)
        data = serializer.data
        return response.Response(data)


class ProfileUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            user = request.user
            serializer.update(user, serializer.validated_data)
            return response.Response(status=status.HTTP_204_NO_CONTENT)

        return response.Response(status=status.HTTP_400_BAD_REQUEST)
