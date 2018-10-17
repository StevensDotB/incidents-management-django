from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    """Model for departments name"""
    class Meta:
        db_table = "departments"

    name = models.CharField(max_length=50)


class UserEmployee(models.Model):
    """User employee"""
    class Meta:
        db_table = "users_employees"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=False)
