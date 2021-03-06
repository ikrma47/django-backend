from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import RegisterUserSerializer, LoginAndObtainTokenSerializer, VerifyEmailAndObtainTokenSerializer
from helper.functions import generateOtp
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

# Create your views here.


class SignupView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        otp = generateOtp()
        request.data['otp'] = otp
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        subject = 'OTP Verification'
        message = f'Your otp is {otp}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.data['email'],]
        send_mail(subject,message,email_from,recipient_list)

        return Response(
            status=status.HTTP_201_CREATED,
            data={
            "success": True,
            "message": "Otp has been sent to your email. please login to continue!",
            "data": []
        })



class LoginView(TokenObtainPairView):
    serializer_class = LoginAndObtainTokenSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        if serializer.validated_data['success'] is True:
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(serializer.validated_data, status=status.HTTP_423_LOCKED)


class VerifyEmailView(TokenObtainPairView):
    serializer_class = VerifyEmailAndObtainTokenSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        if serializer.validated_data['success'] is True:
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(serializer.validated_data, status=status.HTTP_423_LOCKED)