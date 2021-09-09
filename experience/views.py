from rest_framework import viewsets, mixins, status
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Experience
from .serializers import ExperienceSerializer
from rest_framework.response import Response


# Create your views here.

class ExperienceViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):

    permission_classes = [JWTAuthentication]
    authentication_classes = [IsAuthenticated]

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    lookup_field = 'user'

    # override get_object specifically for retrieve method to retrieve all experiences of a user
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        if self.action == 'retrieve':
            return get_list_or_404(queryset, **filter_kwargs)
        else:
            filter_kwargs = {'pk': self.kwargs[lookup_url_kwarg]}
            return get_object_or_404(queryset, **filter_kwargs)

    def retrieve(self, request, *args, **kwargs):
        instances = self.get_object()
        serializer = self.get_serializer(instance=instances, many=True)
        return Response(data={
            'success': True,
            'message': 'Academics updated successfully',
            'data': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT, data={
            'success': True,
            'message': "deleted successfully",
            'data': []
        })
