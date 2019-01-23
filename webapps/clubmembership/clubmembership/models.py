from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    started = models.DateField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Person(models.Model):
    GENDER = (('M', 'Male'),
              ('F', 'Female'),
              ('P', 'Prefer Not to Say'))
    name = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    sex = models.CharField(max_length=1, choices=GENDER)
    membership = models.ManyToManyField(Group, blank="")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Fee(models.Model):
    FEE_LENGTH = ((1, 'ONE TIME'),
                  (7, 'WEEKLY'),
                  (30, 'MONTHLY'),
                  (365, 'YEARLY'))
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    amount = models.FloatField()
    period = models.IntegerField(choices=FEE_LENGTH)
    effective = models.DateField(null=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ('description', 'effective',)
