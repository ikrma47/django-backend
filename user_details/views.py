from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .models import Details, PhoneNumbers, Address
from .serializers import CourseCategorySerializer, DetailsSerializer, DetailsNestedSerializer, ImageSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class DetailsViewSet(viewsets.ModelViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return DetailsNestedSerializer
        return self.serializer_class


class UpdateImage(viewsets.GenericViewSet, mixins.UpdateModelMixin):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Details.objects.all()
    serializer_class = ImageSerializer


class UpdateCourseCategory(viewsets.GenericViewSet, mixins.UpdateModelMixin):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset=Details.objects.all()
    serializer_class = CourseCategorySerializer