from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email", ""),
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    telegram_chat_id = serializers.CharField(
        source="profile.telegram_chat_id", required=False, allow_blank=True
    )

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "telegram_chat_id"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        profile_data = validated_data.pop("profile", {})
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email", ""),
        )
        UserProfile.objects.create(user=user, **profile_data)
        return user
