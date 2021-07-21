from django.db import models
from django.utils import timezone



class Testdata(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Phone_no=models.IntegerField()
    course=models.CharField(max_length=20) 

    class Meta:
       db_table='testdata'

