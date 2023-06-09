#pylint: disable=inconsistent-return-statements
#pylint: disable=wrong-import-order
#pylint: disable=ungrouped-imports
#pylint: disable=missing-function-docstring
#pylint: disable=unused-import
#pylint: disable=no-member
#pylint: disable=bad-whitespace
#pylint: disable=no-else-return
#pylint: disable=bad-continuation
#pylint: disable=missing-module-docstring
#pylint: disable=missing-class-docstring
#pylint: disable=trailing-newlines
from django.db import models
from datetime import datetime


# Create your models here.
class Roles(models.Model):
    RoleId =models.AutoField(primary_key=True)
    RoleNm=models.CharField(max_length=200)

class Project(models.Model):
    ProjectId =models.AutoField(primary_key=True)
    ProjectNm=models.CharField(max_length=200)

class Employee(models.Model):
    Id =models.AutoField(primary_key=True)
    emp_id = models.IntegerField(blank=True)
    emp_name = models.CharField(max_length=255)
    date_time_in = models.CharField(max_length=255)
    date_time_out = models.CharField(max_length=255)
    duration = models.FloatField()
    # hourly_rate = models.FloatField()
    is_approved = models.BooleanField(default=False)
    # RoleId =models.ForeignKey(Roles,on_delete=models.CASCADE)
    ProjectId =models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name

