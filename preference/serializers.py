from rest_framework import serializers
from .models import Preferences, ProgramPreference


class PreferencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Preferences
        fields = ['id', 'preference']


class ProgramPreferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgramPreference
        fields = '__all__'
        lookup_field = 'user'
