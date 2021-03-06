# Generated by Django 3.2.6 on 2021-09-10 14:55

from django.db import migrations
from django.contrib.auth.hashers import make_password


def code(apps, schema_editor):
    User = apps.get_model('authentication', 'User')
    db_alias = schema_editor.connection.alias
    User.objects.using(db_alias).create(email='test@admin.com',
                                        cnic='1234567890556', password=make_password('12345'), isAdmin=True, isVerified=True)


def reverse_code(apps, schema_editor):
    User = apps.get_model('authentication', 'User')
    db_alias = schema_editor.connection.alias
    User.objects.using(db_alias).filter(email='test@admin.com').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_otp'),
    ]

    operations = [
        migrations.RunPython(code, reverse_code)
    ]
