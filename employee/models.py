from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Employee_Info(models.Model):
    status = models.TextField(max_length=255)
    phone = models.TextField(max_length=255)
    date_of_birth = models.DateTimeField()
    employment_type = models.TextField(max_length=255)

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)