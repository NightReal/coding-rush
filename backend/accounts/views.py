from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .permissions import UserAccountViewPermission
from rest_framework import views, response, status


# Create your views here.

class AccountView(views.APIView):
    queryset = User.objects.all()
    permission_classes = (UserAccountViewPermission,)

    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user, many=False)
        return response.Response(serializer.data)


class RegisterView(views.APIView):
    queryset = User.objects.all()

    def post(self, request, format=None):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid(raise_exception=True):
            user = serialized.save()
            return response.Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)