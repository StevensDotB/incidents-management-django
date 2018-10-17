from django.contrib.auth.models import User
from django.db import models


class IncidenceStatus(models.Model):
    class Meta:
        db_table = "incidence_status"

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class IncidenceLevel(models.Model):
    class Meta:
        db_table = "incidence_level"

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Incidence(models.Model):
    class Meta:
        db_table = "incidences"

    subject = models.CharField(max_length=120)
    message = models.TextField(max_length=350)
    user = models.ForeignKey(User, on_delete=False)
    status = models.ForeignKey(IncidenceStatus, on_delete=models.CASCADE, null=True)
    level = models.ForeignKey(IncidenceLevel, on_delete=models.CASCADE, null=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return self.subject


class IncidenceStatusLog(models.Model):
    class Meta:
        db_table = "incidences_status_log"

    user = models.ForeignKey(User, on_delete=False)
    incidence = models.ForeignKey(Incidence, on_delete=False, null=True)
    status = models.ForeignKey(IncidenceStatus, on_delete=False, null=True)
    update = models.DateTimeField(auto_now=True, verbose_name="Update Date")
