from django.db import models

from users.models import User


class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.IntegerField()
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.date} - mood: {self.mood}"
