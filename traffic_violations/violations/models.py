from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Violation(models.Model):
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.description


