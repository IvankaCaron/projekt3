# Generated by Django 2.0 on 2017-12-28 16:10

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20171226_1826'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('noPhone', django.db.models.manager.Manager()),
            ],
        ),
    ]