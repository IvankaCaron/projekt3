# Generated by Django 2.0 on 2017-12-26 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userprofile_city'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
    ]