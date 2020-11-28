from django.db import models

# Create your models here.
class Employees (models.Model):
    EmployeeId=models.AutoField(primary_key = True)
    EmployeeName=models.CharField(max_length=100)
    EmployeeAddress = models.CharField(max_length=255)
    EmployeeEmail=models.EmailField()
    EmployeePhoneNumber=models.IntegerField()
    EmployeeImage = models.ImageField(upload_to="img/%y")