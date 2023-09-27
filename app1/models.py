from django.db import models

# Create your models here.
class Person(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    age=models.IntegerField()
    gender_choice=(('Male','M'),('Female','F'))
    gender=models.CharField(max_length=10,choices=gender_choice,default="")
    address=models.TextField(max_length=100)
    phone=models.CharField(max_length=10,default="")
    
    def __str__(self):
        return f'self.fname'