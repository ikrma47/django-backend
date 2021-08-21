from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from django.db.models import Q
from .serializers import RegisterUserSerializer, MyTokenObtainPairSerializer

# Create your views here.


class SignupView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
