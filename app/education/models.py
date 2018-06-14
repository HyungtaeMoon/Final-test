from django.db import models
from django.utils import timezone


class School(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20)
    create_at = models.DateTimeField(default=timezone.now)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name