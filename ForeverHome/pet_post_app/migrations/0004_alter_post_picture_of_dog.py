# Generated by Django 4.1.7 on 2023-05-02 05:05

from django.db import migrations, models
import pet_post_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_post_app', '0003_alter_post_picture_of_dog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture_of_dog',
            field=models.ImageField(default='default_pfp.png', upload_to=pet_post_app.models.get_profile_image_filepath),
        ),
    ]
