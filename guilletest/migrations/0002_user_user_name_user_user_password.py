# Generated by Django 4.2.1 on 2023-05-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guilletest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='user_password',
            field=models.CharField(default='', max_length=100),
        ),
    ]