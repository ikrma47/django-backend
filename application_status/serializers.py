from rest_framework.serializers import ModelSerializer
from .models import ApplicationStatus


class ApplicationStatusSerializer(ModelSerializer):

    class Meta:
        model = ApplicationStatus
        exclude = ['updatedAt', 'createdAt']
