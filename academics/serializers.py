from rest_framework import serializers
from .models import ExamYear, Academics, UserAcademicRecord


class AcademicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Academics
        exclude = ['examYear', 'createdAt', 'updatedAt']


class ExamYearSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamYear
        exclude = ['createdAt', 'updatedAt']


class UserAcademicRecordPlainSerializer(serializers.ModelSerializer):
    academics = AcademicsSerializer()

    class Meta:
        model = UserAcademicRecord
        exclude = ['createdAt', 'updatedAt']
        lookup_field = 'user'


class UserAcademicRecordNestedSerializer(serializers.ModelSerializer):
    academics = AcademicsSerializer(read_only=True)
    examYear = ExamYearSerializer(read_only=True)

    class Meta:
        model = UserAcademicRecord
        exclude = ['createdAt', 'updatedAt']
        lookup_field = 'user'
