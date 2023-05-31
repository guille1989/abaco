from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

# Create your models here.

#Class for users of application
class User(AbstractUser):
    pass

class TextInputs(models.Model):
    text = models.TextField(max_length=140, default='')
    user_name = models.CharField(max_length=140, default='')
    created_at = models.DateTimeField(auto_now_add=True)

class ScrapingCounter(models.Model):
    count = models.IntegerField()
    scraping_date_at = models.DateTimeField(auto_now_add=True)
    scraping_time = models.CharField(max_length=140, default='')
