# Generated by Django 4.1.7 on 2023-05-04 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging_app', '0004_alter_message_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
    ]
