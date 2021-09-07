from rest_framework.serializers import ModelSerializer
from .models import Documents


class DocumentsSerializer(ModelSerializer):

    class Meta:
        model = Documents
        exclude = ['updatedAt', 'created_at']
