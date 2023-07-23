from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict):
        password = validated_data.pop("password")
        if password:
            instance.set_password(password)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ["id", "username", "full_name", "artistic_name", "password", "email"]
        extra_kwargs = {
            "password": {"write_only": True},
        }
