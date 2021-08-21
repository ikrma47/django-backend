from django.db import models
from department.models import DepartmentProgram, Programs

# Create your models here.


class AcademicTerm(models.Model):

    id = models.AutoField(primary_key=True)
    termName = models.CharField(max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.termName


class Batches(models.Model):

    id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=4)
    isAdmissionOpen = models.BooleanField(default=False)
    academicTerm = models.OneToOneField(
        to=AcademicTerm, on_delete=models.CASCADE, related_name='+')
    programs = models.ManyToManyField(
        DepartmentProgram, through='OfferedPrograms', through_fields=('batch', 'departmentProgram'))
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.year} {self.academicTerm}'


class OfferedPrograms(models.Model):

    id = models.AutoField(primary_key=True)
    batch = models.ForeignKey(
        to=Batches, on_delete=models.CASCADE, related_name='offeredPrograms')
    departmentProgram = models.ForeignKey(
        to=DepartmentProgram, on_delete=models.CASCADE, related_name='+')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.departmentProgram)
