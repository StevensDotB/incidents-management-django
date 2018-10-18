from django.db import models


class Department(models.Model):
    """Model for departments name"""
    class Meta:
        db_table = "departments"

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

