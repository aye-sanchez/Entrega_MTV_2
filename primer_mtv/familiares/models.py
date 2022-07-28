from django.db import models

# Create your models here.

class familiares(models.Model):
    date = models.DateField (auto_now_add = True, null = True, blank = True)
    name = models.CharField(max_length=20, default=True)
    last_name = models.CharField (max_length=20, default=True)
    age = models.IntegerField (default=True)
    gender = models.CharField (max_length= 10, null=True, default=True)
    relationship = models.CharField (max_length=10)

