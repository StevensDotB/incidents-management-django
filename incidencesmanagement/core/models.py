from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    """Model for departments name"""
    name = models.CharField(max_length=50, choices=(
        ('NSE', 'Network and System Engineering'),
        ('SP', 'Support'),
        ('HR', 'Human Resources'),
        ('SD', 'Selling')
    ))


class UserEmployee(models.Model):
    """User employee"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=False)
