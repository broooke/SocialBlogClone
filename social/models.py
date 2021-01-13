from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Group(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.title
    
    def count_comment(self):
        return self.countpost.filter()
    
    def count_members(self):
        return self.countmembers.filter()
    
class Post(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='countpost')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

class members(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='countmembers')

    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ("group", "user")

class User(auth.models.User, auth.models.PermissionsMixin):
    
    def __str__(self):
        return "@"+self.username




