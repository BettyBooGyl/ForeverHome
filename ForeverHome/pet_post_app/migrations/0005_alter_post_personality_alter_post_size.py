# Generated by Django 4.2 on 2023-05-05 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_post_app', '0004_alter_post_picture_of_dog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='personality',
            field=models.CharField(choices=[('COUCH_POTATO', 'Couch potato'), ('ENERGETIC', 'Energetic'), ('SOCIABLE', 'Sociable'), ('CUDDLY', 'Cuddly'), ('PLAYFUL', 'Playful'), ('PROTECTIVE', 'Protective')], default='CALM', max_length=40),
        ),
        migrations.AlterField(
            model_name='post',
            name='size',
            field=models.CharField(choices=[('SM', 'Small'), ('MD', 'Medium'), ('LG', 'Large'), ('XL', 'X-Large')], default='MD', max_length=2),
        ),
    ]
