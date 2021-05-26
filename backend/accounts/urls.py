from django.urls import path
from .views import (
    UserRegisterView,
    UsernameUserExistsView,
    EmailUserExistsView,
    ChangePasswordView,
    PrivateUserProfileView,
    ProfileUpdateView,
    PublicProfileInformationView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('register', UserRegisterView.as_view(), name='registration'),
    path('usernameExists/<str:username>', UsernameUserExistsView.as_view(), name='username exists'),
    path('emailExists/<str:email>', EmailUserExistsView.as_view(), name='email exists'),
    path('changePassword', ChangePasswordView.as_view(), name='change user password'),
    path('getme', PrivateUserProfileView.as_view(), name='get current profile'),
    path('updateProfile', ProfileUpdateView.as_view(), name='profile information update'),
    path('profile/<str:username>', PublicProfileInformationView.as_view(), name='public profile information')
]

urlpatterns = format_suffix_patterns(urlpatterns)
