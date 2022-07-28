from django.db import models

# Create your models here.

class familiares(models.Model):
    name = models.CharField(max_length=20, default=True)
    last_name = models.CharField (max_length=20, default=True)
    date_of_birth = models.DateField (auto_now_add = True, null = True, blank = True)
    age = models.IntegerField (default=True)
    relationship = models.CharField (max_length=10)
    gender = models.CharField (max_length= 10, null=True, default=True)

