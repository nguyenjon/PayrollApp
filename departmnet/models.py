from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)