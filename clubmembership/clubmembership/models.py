from django.db import models


class Person(models.Model):
    GENDER = (('M', 'Male'),
              ('F', 'Female'))
    name = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    sex = models.CharField(max_length=1, choices=GENDER)


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
