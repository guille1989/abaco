# Generated by Django 4.2.1 on 2023-05-26 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guilletest', '0002_user_user_name_user_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_password',
        ),
    ]
