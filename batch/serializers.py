from .models import Batches, AcademicTerm, OfferedPrograms
from rest_framework import serializers
from department.serializers import DetailedSerializer


class AcademicTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicTerm
        fields = '__all__'


class BatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batches
        fields = '__all__'


class OfferedProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferedPrograms
        fields = ['id', 'batch', 'departmentProgram']


class BatchesReadSerializer(serializers.ModelSerializer):

    programs = DetailedSerializer(many=True, read_only=True)
    academicTerm = AcademicTermSerializer(read_only=True)

    class Meta:
        model = Batches
        fields = ['id', 'year', 'academicTerm', 'programs']
        read_only_fields = ('id', 'year', 'academicTerm', 'programs')
