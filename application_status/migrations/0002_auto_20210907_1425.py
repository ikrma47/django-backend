# Generated by Django 3.2.6 on 2021-09-07 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application_status', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationstatus',
            name='id',
        ),
        migrations.AlterField(
            model_name='applicationstatus',
            name='appId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='applicationStatus', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
