from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .models import Details, PhoneNumbers, Address
from .serializers import CourseCategorySerializer, DetailsSerializer, ImageSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class DetailsViewSet(viewsets.ModelViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'user'

    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(data={
            'success': True,
            'message': 'profil details fetched',
            'data': [serializer.data]
        })

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(data={
            'success': True,
            'message': 'details updated successfully',
            'data': [serializer.data]
        })


class UpdateImage(viewsets.GenericViewSet, mixins.UpdateModelMixin):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'user'

    queryset = Details.objects.all()
    serializer_class = ImageSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(data={
            'success': True,
            'message': 'image updated successfully',
            'data': [serializer.data]
        })


class UpdateCourseCategory(viewsets.GenericViewSet, mixins.UpdateModelMixin):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'user'

    queryset = Details.objects.all()
    serializer_class = CourseCategorySerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(data={
            'success': True,
            'message': 'course category updated successfully',
            'data': [serializer.data]
        })
