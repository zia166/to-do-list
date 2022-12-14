from venv import create
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
 
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   
    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    task = models.CharField(max_length=400)

    created = models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["updated", "created"]

    def __str__(self):
        return self.task
