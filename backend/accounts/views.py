from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .permissions import UserAccountViewPermission
from rest_framework import views, response


# Create your views here.

class AccountView(views.APIView):
    queryset = User.objects.all()
    permission_classes = (UserAccountViewPermission,)

    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user, many=False)
        return response.Response(serializer.data)
