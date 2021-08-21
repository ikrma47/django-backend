# Generated by Django 3.2.6 on 2021-08-18 13:14

from django.db import migrations


def code(apps, schema_editor):

    Preferences = apps.get_model('preference', 'Preferences')
    alias = schema_editor.connection.alias
    Preferences.objects.using(alias).bulk_create([
        Preferences(preference='1st'),
        Preferences(preference='2nd'),
        Preferences(preference='3rd'),
        Preferences(preference='4th'),
        Preferences(preference='5th'),
    ])


def reverse_code(apps, schema_editor):

    Preferences = apps.get_model('preference', 'Preferences')
    alias = schema_editor.connection.alias
    Preferences.objects.using(alias).filter(preference='1st').delete()
    Preferences.objects.using(alias).filter(preference='2nd').delete()
    Preferences.objects.using(alias).filter(preference='3rd').delete()
    Preferences.objects.using(alias).filter(preference='4th').delete()
    Preferences.objects.using(alias).filter(preference='5th').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('preference', '0003_auto_20210812_0853'),
    ]

    operations = [
        migrations.RunPython(code, reverse_code)
    ]
