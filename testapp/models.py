from django.db import models

# Create your models here.
class contactInfo(models.Model):
    Name=models.CharField(max_length=30)
    email=models.EmailField()
    addr=models.CharField(max_length=60)
    class Meta:
        abstract=True
class student(contactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()
class teacher(contactInfo):
    subject=models.CharField(max_length=30)
    salary=models.FloatField()