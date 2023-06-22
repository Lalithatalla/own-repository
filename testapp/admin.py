class ContactInfo(models.Model):
    Name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=64)
    class Meta:
        abstract = True

class Student(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher(ContactInfo):
    subject = models.CharField(max_length=30)
    salary = models.FloatField()