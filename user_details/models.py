from django.db import models
from datetime import datetime
from django.conf import settings


class Details(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    fatherName = models.CharField(max_length=70)
    dob = models.DateField(max_length=10)
    domicile = models.CharField(max_length=30)
    religion = models.CharField(max_length=20)
    image = models.CharField(max_length=255)
    courseCategory = models.CharField(max_length=3)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='details')


class PhoneNumbers(models.Model):

    id = models.AutoField(primary_key=True)
    details = models.OneToOneField(
        to=Details, related_name='phoneNumbers', on_delete=models.CASCADE)
    primaryPhoneNumber = models.CharField(max_length=20)
    secondaryPhoneNumber = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Address(models.Model):

    id = models.AutoField(primary_key=True)
    mailingAddress = models.CharField(max_length=255)
    residentialAddress = models.CharField(max_length=255)
    details = models.OneToOneField(
        to=Details, on_delete=models.CASCADE, related_name='address')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
