from django.db import models
from django.conf import settings

# Create your models here.


class ExamYear(models.Model):

    id = models.AutoField(primary_key=True)
    examination = models.CharField(max_length=15)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Academics(models.Model):

    id = models.AutoField(primary_key=True)
    yearHeld = models.CharField(max_length=4)
    obtainedMarks = models.CharField(max_length=3)
    maxMarks = models.CharField(max_length=4)
    cgpa = models.CharField(max_length=4)
    awards = models.CharField(max_length=255)
    majors = models.CharField(max_length=255)
    institue = models.CharField(max_length=255)
    examYear = models.ManyToManyField(
        to=ExamYear,
        through='UserAcademicRecord',
        related_name='academics',
        through_fields=('academics', 'examYear'))
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class UserAcademicRecord(models.Model):

    id = models.AutoField(primary_key=True)
    examYear = models.ForeignKey(
        ExamYear,
        on_delete=models.CASCADE,
        related_name='academicRecord')
    academics = models.ForeignKey(
        Academics,
        on_delete=models.CASCADE,
        related_name='academics')
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="userAcademicRecords")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
