from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=300)  # Use lowercase 'title' for field names
    description = models.TextField(default='')
    private = models.BooleanField(default=False) 
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)   # Linking tasks to a specific user

    def __str__(self) :
        return self.title
    

