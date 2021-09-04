from rest_framework import viewsets
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Experience
from .serializers import ExperienceSerializer
from rest_framework.response import Response


# Create your views here.

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
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