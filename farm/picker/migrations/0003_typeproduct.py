# Generated by Django 2.0 on 2018-01-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0002_spot_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('icon', models.ImageField(blank=True, upload_to='icon_image')),
            ],
        ),
    ]
