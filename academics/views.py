from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserAcademicRecordNestedSerializer, UserAcademicRecordPlainSerializer
from .models import UserAcademicRecord
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class UserAcademicRecordView(viewsets.ModelViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserAcademicRecord.objects.all()
    serializer_class = UserAcademicRecordNestedSerializer
    lookup_field = 'user'

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return self.serializer_class
        return UserAcademicRecordPlainSerializer

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
        instances = self.get_object(kwargs['pk'])
        serializer = self.get_serializer(many=True, instance=instances)
        return Response(data=serializer.data)
