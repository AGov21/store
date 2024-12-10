from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images')
    phone = models.CharField(max_length=64)


    def __str__(self):
        return self.username
