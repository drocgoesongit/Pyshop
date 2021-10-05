from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=300)
    rollNo = models.IntegerField()
