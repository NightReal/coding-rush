from django.contrib.auth import get_user_model, password_validation
from rest_framework import serializers
from django.contrib.auth.models import BaseUserManager
from django.core.files.images import get_image_dimensions
from django.conf import settings

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering the user
    """
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name', 'password_confirm')
        read_only_fields = ('id',)
        write_only_fields = ('password',)
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True},
        }

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                "password_confirm": ("Passwords didn't match",),
            })

        return attrs

    def create(self, validated_data):
        # TODO: email confirmation
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint
    """
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    new_password_confirm = serializers.CharField(required=True, write_only=True)

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value

    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate(self, data):
        if data['new_password'] != data['new_password_confirm']:
            raise serializers.ValidationError({
                "new_password_confirm": ("Passwords didn't match",),
            })
        return data

    def update(self, **kwargs):
        password = self.validated_data['new_password']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user


class PrivateProfileInformationSerializer(serializers.ModelSerializer):
    """
    Serializer for private info retrieving endpoint
    """

    class Meta:
        model = User
        fields = ('avatar', 'email', 'username', 'first_name', 'last_name', 'last_login')


class ProfileUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for profile update endpoint
    """

    class Meta:
        model = User
        fields = ('avatar', 'first_name', 'last_name')

    def validate_avatar(self, value):
        if value is None:
            return value
        w, h = get_image_dimensions(value)
        if w <= settings.MAX_AVATAR_SIZE and h <= settings.MAX_AVATAR_SIZE:
            return value
        raise serializers.ValidationError('Avatar is too big')
