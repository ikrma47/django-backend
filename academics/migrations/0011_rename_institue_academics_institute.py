# Generated by Django 3.2.6 on 2021-09-09 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0010_auto_20210909_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academics',
            old_name='institue',
            new_name='institute',
        ),
    ]
