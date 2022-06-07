from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    desc = models.CharField(max_length=100)
    timestamp = models.DateTimeField()