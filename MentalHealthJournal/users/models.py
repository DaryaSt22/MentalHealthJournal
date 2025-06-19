from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True, null=True)
    timezone = models.CharField(max_length=100, blank=True, null=True)
    #image = models.ImageField(upload_to='users_image', null=True, blank=True)

    def __str__(self):
        return self.username


