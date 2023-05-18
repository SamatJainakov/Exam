from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return self.username


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name
