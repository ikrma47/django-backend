from rest_framework import viewsets, mixins
from .serializers import DocumentsSerializer
from .models import Documents
from rest_framework.response import Response

# Create your views here.


class DocumentsView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):

    serializer_class = DocumentsSerializer
    queryset = Documents.objects.all()
