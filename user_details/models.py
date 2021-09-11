from django.db import models
from django.conf import settings


class Details(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, null=True)
    fatherName = models.CharField(max_length=70, null=True)
    dob = models.DateField(max_length=10, null=True)
    domicile = models.CharField(max_length=30, null=True)
    religion = models.CharField(max_length=20, null=True)
    image = models.CharField(max_length=255, null=True)
    courseCategory = models.CharField(max_length=3, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='detail')


class PhoneNumbers(models.Model):

    id = models.AutoField(primary_key=True)
    details = models.OneToOneField(
        to=Details, related_name='phoneNumber', on_delete=models.CASCADE)
    primaryPhoneNumber = models.CharField(max_length=20, null=True)
    secondaryPhoneNumber = models.CharField(max_length=20, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Address(models.Model):

    id = models.AutoField(primary_key=True)
    mailingAddress = models.CharField(max_length=255, null=True)
    residentialAddress = models.CharField(max_length=255, null=True)
    details = models.OneToOneField(
        to=Details, on_delete=models.CASCADE, related_name='address')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
