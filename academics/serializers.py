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
        read_only_fields = ['user', 'examYear']
        lookup_field = 'user'

    def update(self, instance, validated_data):
        academics = instance.academics
        academics.yearHeld = validated_data['academics'].get(
            'yearHeld', academics.yearHeld)
        academics.obtainedMarks = validated_data['academics'].get(
            'obtainedMarks', academics.obtainedMarks)
        academics.maxMarks = validated_data['academics'].get(
            'maxMarks', academics.maxMarks)
        academics.cgpa = validated_data['academics'].get(
            'cgpa', academics.cgpa)
        academics.awards = validated_data['academics'].get(
            'awards', academics.awards)
        academics.majors = validated_data['academics'].get(
            'majors', academics.majors)

        academics.save()
        return instance


class UserAcademicRecordNestedSerializer(serializers.ModelSerializer):
    academics = AcademicsSerializer(read_only=True)
    examYear = ExamYearSerializer(read_only=True)

    class Meta:
        model = UserAcademicRecord
        exclude = ['createdAt', 'updatedAt']
        lookup_field = 'user'
