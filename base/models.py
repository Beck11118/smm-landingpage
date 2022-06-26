from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)

class Discount(models.Model):
    unit = models.IntegerField()
    date_until = models.DateTimeField()

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    priority = models.IntegerField(default=1)


class Lead(models.Model):
    fio = models.CharField(max_length=200)
    phone = models.IntegerField()
    company = models.BooleanField(default=False)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    inn = models.IntegerField(blank=True, null=True)




