from django.db import models
from django.apps import apps
from django.contrib.auth.models import User


class UserEmployee(models.Model):
    """User employee"""
    class Meta:
        db_table = "users_employees"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('department.Department', null=True, on_delete=False)
