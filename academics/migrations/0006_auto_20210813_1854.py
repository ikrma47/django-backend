# Generated by Django 3.2.6 on 2021-08-13 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0005_auto_20210813_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academics',
            old_name='examination',
            new_name='examYear',
        ),
        migrations.RenameField(
            model_name='useracademicrecord',
            old_name='examination',
            new_name='examYear',
        ),
    ]
