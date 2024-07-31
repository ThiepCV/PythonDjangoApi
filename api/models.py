from django.db import models

# Create your models here.


class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField()
    biography = models.TextField()
    mothersMaidenName = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.firstName} - {self.lastName}"
    
class Teacher(models.Model):
     name = models.CharField(max_length=80)

     def __str__(self):
            return f"{self.name}"

class Course(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="course")  
    def __str__(self):
        return f"{self.title}"
    
class Candidate(models.Model):
     name = models.CharField(max_length=100)
     courses = models.ManyToManyField(Course, related_name="students")

     def __str__(self):
        return f"{self.name}"
