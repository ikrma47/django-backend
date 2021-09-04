# Generated by Django 3.2.6 on 2021-08-10 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Academics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('yearHeld', models.CharField(max_length=4)),
                ('obtainedMarks', models.CharField(max_length=3)),
                ('maxMarks', models.CharField(max_length=4)),
                ('cgpa', models.CharField(max_length=4)),
                ('awards', models.CharField(max_length=255)),
                ('majors', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExamYear',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('examination', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserAcademicRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('academics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.academics')),
                ('examYear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.examyear')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userAcademicRecords', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='academics',
            name='userAcademicRecords',
            field=models.ManyToManyField(through='academics.UserAcademicRecord', to='academics.ExamYear'),
        ),
    ]