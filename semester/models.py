from django.db import models
from django.conf import settings
from batch.models import AcademicTerm, Batches
from department.models import DepartmentProgram

# Create your models here.


class Semester(models.Model):

    id = models.AutoField(primary_key=True)
    semester = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)


class SemesterDetail(models.Model):

    id = models.AutoField(primary_key=True)
    academicTerm = models.ForeignKey(
        to=AcademicTerm, on_delete=models.CASCADE, related_name='+')
    batch = models.ForeignKey(
        to=Batches, on_delete=models.CASCADE, related_name='semesterDetails')
    departmentProgram = models.ForeignKey(
        to=DepartmentProgram, on_delete=models.CASCADE, related_name='semesterDetails')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class SemesterCourses(models.Model):

    id = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=30)
    courseCode = models.CharField(max_length=10)
    isUniElective = models.BooleanField(default=False)
    isStudentElective = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class OfferedCourses(models.Model):

    id = models.AutoField(primary_key=True)
    semesterDetail = models.ForeignKey(
        to=SemesterDetail, on_delete=models.CASCADE, related_name='offeredCourses')
    semesterCourse = models.ForeignKey(
        to=SemesterCourses, on_delete=models.CASCADE, related_name='+')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class SemesterEnrollment(models.Model):

    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='semesterEnrollment')
    semesterDetail = models.ForeignKey(
        to=SemesterDetail, on_delete=models.CASCADE, related_name='semesterEnrollment')
    isCompleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
