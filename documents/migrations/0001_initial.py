# Generated by Django 3.2.6 on 2021-09-07 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0003_alter_user_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('appId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='documents', serialize=False, to='authentication.user')),
                ('cnicFront', models.CharField(max_length=255, null=True)),
                ('cnicBack', models.CharField(max_length=255, null=True)),
                ('matricCertificate', models.CharField(max_length=255, null=True)),
                ('intermediateCertificate', models.CharField(max_length=255, null=True)),
                ('firstSemesterDmc', models.CharField(max_length=255, null=True)),
                ('secondSemesterDmc', models.CharField(max_length=255, null=True)),
                ('thirdSemesterDmc', models.CharField(max_length=255, null=True)),
                ('fourthSemesterDmc', models.CharField(max_length=255, null=True)),
                ('fifthSemesterDmc', models.CharField(max_length=255, null=True)),
                ('sixthSemesterDmc', models.CharField(max_length=255, null=True)),
                ('seventhSemesterDmc', models.CharField(max_length=255, null=True)),
                ('eighthSemesterDmc', models.CharField(max_length=255, null=True)),
                ('bsCertificate', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
