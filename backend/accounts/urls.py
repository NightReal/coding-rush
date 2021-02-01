from django.urls import path
from .views import (
    PrivateAccountView,
    RegisterView,
    UsernameUserExistsView,
    EmailUserExistsView,
    PublicAccountView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('getme/', PrivateAccountView.as_view(), name='getme'),
    path('profile/<str:username>/', PublicAccountView.as_view(), name='Statistics of profile'),
    path('register/', RegisterView.as_view(), name='registration'),
    path('usernameExists/<str:username>', UsernameUserExistsView.as_view(), name='username exists'),
    path('emailExists/<str:email>', EmailUserExistsView.as_view(), name='email exists'),
]
