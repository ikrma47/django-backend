from rest_framework import viewsets
from .serializers import OfferedProgramsSerializer, BatchesSerializer, BatchesReadSerializer
from .models import OfferedPrograms, Batches


class OfferedProgramsViewSet(viewsets.ModelViewSet):

    queryset = OfferedPrograms.objects.all()
    serializer_class = OfferedProgramsSerializer


class BatchViewSet(viewsets.ModelViewSet):

    queryset = Batches.objects.all()
    serializer_class = BatchesSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return BatchesReadSerializer
        else:
            return self.serializer_class
