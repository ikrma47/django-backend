from django.db import models
from django.conf import settings

# Create your models here.


class Experience(models.Model):

    id = models.AutoField(primary_key=True)
    jobTitle = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    salary = models.IntegerField()
    duty = models.CharField(max_length=50)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="experiences")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
