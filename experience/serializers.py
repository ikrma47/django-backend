from rest_framework import serializers
from .models import Experience


class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        exclude = ['createdAt', 'updatedAt']
