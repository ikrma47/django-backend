from django.db import models
from authentication.models import User

# Create your models here.


class ApplicationStatus(models.Model):

    appId = models.OneToOneField(
        to=User, on_delete=models.CASCADE, related_name='applicationStatus')
    isProfile = models.BooleanField(default=False, null=False)
    isCourseCategory = models.BooleanField(default=False, null=False)
    isFirstYear = models.BooleanField(default=False, null=False)
    isSecondYear = models.BooleanField(default=False, null=False)
    isThirdYear = models.BooleanField(default=False, null=False)
    isFinalYear = models.BooleanField(default=False, null=False)
    isGAT = models.BooleanField(default=False, null=False)
    isMS = models.BooleanField(default=False, null=False)
    isExperience = models.BooleanField(default=False, null=False)
    isPreference = models.BooleanField(default=False, null=False)
    isCnicFront = models.BooleanField(default=False, null=False)
    isCnicBack = models.BooleanField(default=False, null=False)
    isMatricCertificate = models.BooleanField(default=False, null=False)
    isIntermediateCertificate = models.BooleanField(default=False, null=False)
    isFirstSemesterDmc = models.BooleanField(default=False, null=False)
    isSecondSemesterDmc = models.BooleanField(default=False, null=False)
    isThirdSemesterDmc = models.BooleanField(default=False, null=False)
    isFourthSemesterDmc = models.BooleanField(default=False, null=False)
    isFifthSemesterDmc = models.BooleanField(default=False, null=False)
    isSixthSemesterDmc = models.BooleanField(default=False, null=False)
    isSeventhSemesterDmc = models.BooleanField(default=False, null=False)
    isEighthSemesterDmc = models.BooleanField(default=False, null=False)
    isBsCertificate = models.BooleanField(default=False, null=False)
    isSubmitted = models.BooleanField(default=False, null=False)
    isAccepted = models.BooleanField(default=False, null=False)
    comments = models.CharField(max_length=255, null=True)
    acceptedBy = models.CharField(max_length=50, null=True)
    rejectedBy = models.BooleanField(max_length=50, null=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
