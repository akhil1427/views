from django.db import models

# Create your models here.
class school(models.Model):
    sname=models.CharField(max_length=100)
    spric=models.CharField(max_length=100)
    
