from rest_framework import viewsets, mixins
from .serializers import DocumentsSerializer
from .models import Documents
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class DocumentsView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = DocumentsSerializer
    queryset = Documents.objects.all()
    lookup_field = 'appId'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(data={
            'success': True,
            'message': 'documents fetched',
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
            'message': 'documents updated successfully',
            'data': [serializer.data]
        })
