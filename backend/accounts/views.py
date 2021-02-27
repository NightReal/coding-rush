from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import caches

from .serializers import (
    PrivateUserSerializer,
    RegisterSerializer,
    PublicUserSerializer,
)
from rest_framework import (
    views,
    response,
    status,
    permissions
)

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# Create your views here.

class PrivateAccountView(views.APIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, **kwargs):
        user = request.user
        data = caches['privateAccountInfo'].get(user.id)
        if data is None:
            serializer = UserSerializer(user, many=False)
            data = serializer.data
            caches['privateAccountInfo'].set(user.id, data, CACHE_TTL)
        return response.Response(data)

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


class RegisterView(views.APIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            caches['usernameExists'].delete(request.data['username'])
            caches['emailExists'].delete(request.data['email'])
            return response.Response(serializer.data, status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UsernameUserExistsView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, username: str, *args, **kwargs):
        res = caches['usernameExists'].get(username)
        if res is None:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                res = {'username': False}
            else:
                res = {'username': True}
            caches['usernameExists'].set(username, res, CACHE_TTL)
        return response.Response(res)


class EmailUserExistsView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, email: str, *args, **kwargs):
        res = caches['emailExists'].get(email)
        if res is None:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                res = {'email': False}
            else:
                res = {'email': True}
            caches['emailExists'].set(email, res, CACHE_TTL)
        return response.Response(res)
