from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from .models import Details, PhoneNumbers, Address
from .serializers import DetailsSerializer, DetailsNestedSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class Details(viewsets.ModelViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return DetailsNestedSerializer
        return self.serializer_class
