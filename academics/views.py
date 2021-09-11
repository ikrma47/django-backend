from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from .serializers import UserAcademicRecordSerializer
from .models import UserAcademicRecord
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class UserAcademicRecordView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserAcademicRecord.objects.all()
    serializer_class = UserAcademicRecordSerializer
    lookup_field = 'user'

    # overriding get_object specifically for retrieve method to retrieve all academics of a user
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
        serializer = self.get_serializer(many=True, instance=instances)
        return Response(data={
            'success': True,
            'message': 'Academics details fetched',
            'data': serializer.data
        })

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # retrieving academics records of user after updating a specific one
        self.action = 'retrieve'
        self.kwargs[self.lookup_field] = serializer.data['user']
        return self.retrieve(request, args, kwargs)
