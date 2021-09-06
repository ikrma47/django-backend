from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from user_details.models import Details, PhoneNumbers, Address
from experience.models import Experience
from academics.models import UserAcademicRecord, Academics, ExamYear
from django.db.models import Q


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'cnic', 'password', 'isAdmin', 'otp']
        extra_kwargs = {
            'password': {'write_only': True},
            'isAdmin': {'default': False},
            'otp': { 'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class LoginAndObtainTokenSerializer(TokenObtainPairSerializer):

    def get_token(cls, user):
        token = super().get_token(user)

        token['isAdmin'] = user.isAdmin

        return token

    def validate(self, attrs):
        super().validate(attrs)
        if self.user.isVerified is True:

            refresh = self.get_token(self.user)

            return {
                "success": True,
                "message": "Logged In",
                "data": [{
                    "email": self.user.email,
                    "isAdmin": self.user.isAdmin,
                    "appId": self.user.appId,
                    "access": str(refresh.access_token),
                    "isVerified": self.user.isVerified,
                    "refresh": str(refresh)
                }]
            }

        return {
            "success": False,
            "message": "please verify your email first",
            "data": [{"email":self.user.email}]
        }

class VerifyEmailAndObtainTokenSerializer(TokenObtainPairSerializer):

    def get_token(cls, user):
        token = super().get_token(user)

        token['isAdmin'] = user.isAdmin

        return token


    def validate(self, attrs):
        super().validate(attrs)

        if (self.user.otp == self.initial_data.get('otp',None)):
            User.objects.filter(
                Q(email=self.initial_data['email']) | Q(otp=self.initial_data['otp'])
            ).update(otp=None, isVerified=True)

            # intializing candidate related models

            details_instance=Details.objects.create(user=self.user)
            PhoneNumbers.objects.create(details=details_instance)
            Address.objects.create(details=details_instance)
            
            for exam_year in ExamYear.objects.all():
                academic_instance = Academics.objects.create()
                UserAcademicRecord.objects.create(examYear=exam_year, academics=academic_instance,user=self.user)
                
            Experience.objects.create(user=self.user)

            refresh = self.get_token(self.user)
            
            return {
                "success": True,
                "message": "Logged In",
                "data": [{
                    "email": self.user.email,
                    "isAdmin": self.user.isAdmin,
                    "appId": self.user.appId,
                    "access": str(refresh.access_token),
                    "isVerified": True,
                    "refresh": str(refresh)
                }]
            }
        return {
            "success": False,
            "message": "Invalid Otp. Try Again",
            "data": []
        }