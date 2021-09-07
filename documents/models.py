from django.db import models
from django.conf import settings
# Create your models here.


class Documents(models.Model):

    appId = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='documents', primary_key=True)
    cnicFront = models.CharField(max_length=255, null=True)
    cnicBack = models.CharField(max_length=255, null=True)
    matricCertificate = models.CharField(max_length=255, null=True)
    intermediateCertificate = models.CharField(max_length=255, null=True)
    firstSemesterDmc = models.CharField(max_length=255, null=True)
    secondSemesterDmc = models.CharField(max_length=255, null=True)
    thirdSemesterDmc = models.CharField(max_length=255, null=True)
    fourthSemesterDmc = models.CharField(max_length=255, null=True)
    fifthSemesterDmc = models.CharField(max_length=255, null=True)
    sixthSemesterDmc = models.CharField(max_length=255, null=True)
    seventhSemesterDmc = models.CharField(max_length=255, null=True)
    eighthSemesterDmc = models.CharField(max_length=255, null=True)
    bsCertificate = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
