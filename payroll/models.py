from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Payroll(models.Model):
    pay = models.DecimalField(max_digits=10, decimal_places=2)
    payroll_type = models.TextField(max_length=255)
    payment_method = models.TextField(max_length=255)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Payslip(models.Model):
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)
    gross_pay = models.DecimalField(max_digits=10, decimal_places=2)
    start_period = models.DateTimeField()
    end_period = models.DateTimeField()

    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE, primary_key=True)

class Raise(models.Model):
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    gross_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()

    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE, primary_key=True)

class Bonus(models.Model):
    previous_pay = models.DecimalField(max_digits=10, decimal_places=2)
    percent_increase = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField()

    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE, primary_key=True)