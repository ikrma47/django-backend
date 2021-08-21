# Generated by Django 3.2.6 on 2021-08-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='appId',
        ),
        migrations.AddField(
            model_name='user',
            name='isVerified',
            field=models.BooleanField(default=False),
        ),
    ]
