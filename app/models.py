from django.db import models
from . models import *
from django.contrib.auth.models import User


# Create your models here.
class category(models.Model):
    name=models.TextField()
    