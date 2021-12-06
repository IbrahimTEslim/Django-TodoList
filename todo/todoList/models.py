from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Todo(models.Model):
    text = models.CharField(max_length=1000)
    is_done = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    done_at = models.DateTimeField(default=None,null=True,blank=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
