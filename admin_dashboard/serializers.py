from rest_framework import serializers
from user_details.models import Details
from authentication.models import User
from application_status.models import ApplicationStatus


class ApplicationStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationStatus
        fields = ['isSubmitted', 'isAccepted', 'rejectedBy', 'acceptedBy']


class ApplicantSerializer(serializers.ModelSerializer):

    applicationStatus = ApplicationStatusSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['appId', 'cnic', 'applicationStatus']


class AdminDashboardSerializer(serializers.ModelSerializer):

    user = ApplicantSerializer(read_only=True)

    class Meta:
        model = Details
        fields = ['name', 'image', 'courseCategory', 'user']
