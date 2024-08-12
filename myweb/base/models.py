from django.db import models
from django.contrib.auth.models import AbstractUser


class Type(models.Model):
    type = models.CharField(max_length=1)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.type


# Create your models here.
class Note(models.Model):
    creator = models.ForeignKey('User', on_delete=models.SET("Unknown User"))
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)  # when created

    class Meta:
        ordering = ['type', '-created']

    def __str__(self):
        return f"{self.name} _ {self.created}"


class User(AbstractUser):
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")



