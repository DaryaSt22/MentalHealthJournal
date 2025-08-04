import uuid

from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models


class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True, null=True)
    timezone = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='users_image', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], blank=True)
    goals = models.TextField(blank=True)
    stress_level = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    day = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    activity = models.TextField(blank=True)
    gratitude = models.TextField(blank=True)
    mood = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.date()}"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = "Profiles"  # для админ


class EmailVerification(models.Model):
    code = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()
    email = models.EmailField(blank=False, null=False)


    def __str__(self):
        return f"EmailVerification object for {self.user.email}"


    def send_verification_email(self):
        send_mail(
            'Subject here',
            'Test verification email',
            'from@example.com',
            [self.user.email],
            fail_silently=False,
        )
