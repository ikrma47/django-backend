# Generated by Django 3.2.6 on 2021-08-18 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0008_alter_useracademicrecord_academics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useracademicrecord',
            name='academics',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academics', to='academics.academics'),
        ),
    ]
