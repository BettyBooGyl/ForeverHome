# Generated by Django 4.1.7 on 2023-05-04 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_profile_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='contacts',
        ),
    ]
