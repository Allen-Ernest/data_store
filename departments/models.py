from django.db import models
from django.contrib import messages

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    hod = models.CharField(max_length=50, unique=True)