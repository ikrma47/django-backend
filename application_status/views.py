from rest_framework import viewsets, mixins
from .serializers import ApplicationStatusSerializer
from .models import ApplicationStatus
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class ApplicationStatusView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ApplicationStatusSerializer
    queryset = ApplicationStatus.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(data={
            'success': True,
            'message': 'successfully fetched',
            'data': [serializer.data],
        })
