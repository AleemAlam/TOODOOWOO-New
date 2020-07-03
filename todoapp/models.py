from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length = 100)
    memo = models.TextField()
    important = models.CheckConstraint()
    complete = models.BooleanField()
    date = models.DateTimeField()
