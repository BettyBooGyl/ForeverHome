# Generated by Django 4.1.7 on 2023-04-20 00:41

from django.db import migrations, models
import profile_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/profile_app/default_pfp.png', max_length=255, null=True, upload_to=profile_app.models.get_profile_image_filepath),
        ),
    ]
