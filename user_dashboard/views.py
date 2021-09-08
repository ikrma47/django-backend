from rest_framework import viewsets, mixins
from .serializers import DashboardSerializer
from user_details.models import Details
from rest_framework.response import Response

# Create your views here.


class DashboardView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):

    serializer_class = DashboardSerializer
    queryset = Details.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(data={
            'success': True,
            'message': 'successfully fetched',
            'data': [serializer.data],
        })
