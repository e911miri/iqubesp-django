from django.db import models
from django.contrib.auth.models import User
from operations.models import Course

# Create your models here.
class StudentCourse(models.Model):
    student = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    paid = models.BooleanField()
    
class Payment(models.Model):
    student = models.ForeignKey(StudentCourse)
    payment_method = models.CharField(max_length=100)
    status = models.CharField(max_length=10)