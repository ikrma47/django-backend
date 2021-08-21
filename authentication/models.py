from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    appId = models.AutoField(primary_key=True)
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(max_length=70, unique=True)
    cnic = models.CharField(max_length=13, unique=True)
    otp = models.CharField(max_length=6)
    isAdmin = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.appId)
