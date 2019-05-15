from django.contrib.auth.models import User
from django.db import models
class Todo(models.Model):
    user = models.ForeignKey(User,related_name='userList',on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user.id) +" - "+ self.task

# Create your models here.
