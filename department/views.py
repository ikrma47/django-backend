from rest_framework import viewsets
from .models import Departments, Programs, DepartmentProgram
from .serializers import DepartmentsSerializer, ProgramsSerializer, DepartmentProgramSerializer, DetailedSerializer
from django_backend.permissions import IsAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class DepartmentViewSet(viewsets.ModelViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class ProgramsViewSet(viewsets.ModelViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    queryset = Programs.objects.all()
    serializer_class = ProgramsSerializer


class DepartmentProgramViewSet(viewsets.ModelViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    queryset = DepartmentProgram.objects.all()
    serializer_class = DepartmentProgramSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retireve':
            return DetailedSerializer
        return self.serializer_class
