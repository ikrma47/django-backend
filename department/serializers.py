from .models import Departments, Programs, DepartmentProgram
from rest_framework import serializers


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id', 'departmentName']


class ProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programs
        fields = ['id', 'programName']


class DepartmentProgramSerializer(serializers.ModelSerializer):
    program = ProgramsSerializer()

    class Meta:
        model = DepartmentProgram
        fields = ['id', 'department', 'program', 'courseCategory']

    def create(self, validated_data):
        program = validated_data.pop('program', None)
        department = Departments.objects.get(
            departmentName=validated_data['department'])
        program = Programs.objects.create(programName=program['programName'])
        departmentProgram = DepartmentProgram.objects.create(
            program=program,
            department=department,
            courseCategory=validated_data['courseCategory'])
        return departmentProgram


class DetailedSerializer(serializers.ModelSerializer):

    program = ProgramsSerializer()
    department = DepartmentsSerializer()

    class Meta:
        model = DepartmentProgram
        fields = ['id', 'department', 'program', 'courseCategory']
