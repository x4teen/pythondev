from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Resource(models.Model):
    RESOURCE_TYPES = (('L', 'Labor'),
                      ('M', 'Material'),
                      ('E', 'Equipment'),
                      ('I', 'Overhead'))

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=1, choices=RESOURCE_TYPES)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)