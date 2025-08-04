from django.db import models

from users.models import User


class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.IntegerField()
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.date} - mood: {self.mood}"


class DailyEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goals = models.TextField(blank=True)
    stress_level = models.IntegerField(null=True, blank=True)
    day = models.TextField(blank=True)
    activity = models.TextField(blank=True)
    gratitude = models.TextField(blank=True)
    mood = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.date()}"
