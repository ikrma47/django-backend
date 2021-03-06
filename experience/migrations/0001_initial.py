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
            name='Experience',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('jobTitle', models.CharField(max_length=50)),
                ('organization', models.CharField(max_length=100)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('salary', models.IntegerField()),
                ('duty', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
