from django.db import models
from django.conf import settings
from batch.models import OfferedPrograms

# Create your models here.


class Preferences(models.Model):

    id = models.AutoField(primary_key=True)
    preference = models.CharField(max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.preference


class ProgramPreference(models.Model):

    id = models.AutoField(primary_key=True)
    preference = models.ForeignKey(
        to=Preferences, on_delete=models.CASCADE, related_name='+')
    offeredProgram = models.ForeignKey(
        to=OfferedPrograms, on_delete=models.CASCADE, related_name='+')
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='preferences')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
