# Generated by Django 3.2.6 on 2021-09-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0009_alter_phonenumbers_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='mailingAddress',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='residentialAddress',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='courseCategory',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='domicile',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='fatherName',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='name',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='religion',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='phonenumbers',
            name='primaryPhoneNumber',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='phonenumbers',
            name='secondaryPhoneNumber',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
