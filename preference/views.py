from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import PreferencesSerializer, ProgramPreferenceSerializer
from .models import Preferences, ProgramPreference

# Create your views here.


class ProgramPreferenceViewSet(viewsets.ModelViewSet):

    queryset = ProgramPreference.objects.all()
    serializer_class = ProgramPreferenceSerializer
    lookup_field = 'user'

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
        return Response(data=serializer.data)


class PreferenceListViewSet(viewsets.ModelViewSet):

    queryset = Preferences.objects.all()
    serializer_class = PreferencesSerializer
