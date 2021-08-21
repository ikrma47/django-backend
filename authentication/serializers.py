from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from django.db.models import Q


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'cnic', 'password', 'isAdmin']
        extra_kwargs = {
            'password': {'write_only': True},
            'isAdmin': {'default': False}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def get_token(cls, user):
        token = super().get_token(user)

        token['isAdmin'] = user.isAdmin

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data = {
            "success": True,
            "message": "Logged In",
            "data": [{
                "email": self.user.email,
                "isAdmin": self.user.isAdmin,
                "appId": self.user.appId,
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }]
        }

        return data
