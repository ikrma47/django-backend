from rest_framework.serializers import ModelSerializer
from user_details.models import Details
from authentication.serializers import RegisterUserSerializer


class DashboardSerializer(ModelSerializer):

    user = RegisterUserSerializer(read_only=True)

    class Meta:
        model = Details
        exclude = ['createdAt', 'updatedAt']
