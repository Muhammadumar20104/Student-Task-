from django.db import models

class Student(models.Model):
    Name=models.CharField(max_length=15)
    Father_Name=models.CharField(max_length=20)
    Phone_No=models.IntegerField(max_length=11, null=True)
    CNIC=models.IntegerField(max_length=14, unique=True)
    def __str__(self):
        return self.Name


class Courses(models.Model):
    Course_Name=models.CharField(max_length=50)
    Course_Fee=models.IntegerField()
    Course_Discription=models.TextField()
    Course_Create=models.DateField(auto_now=False)
    Student=models.ForeignKey(Student,on_delete=models.CASCADE)
    def __str__(self):
        return self.Course_Name
# Create your models here.
