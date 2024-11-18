from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Event model
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_datetime = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='events/photos/', blank=True, null=True)
    organized_by = models.CharField(max_length=255, default="Anonymous")
    participants = models.ManyToManyField(User, related_name="registered_events", blank=True)

    def __str__(self):
        return f"{self.title} organized by {self.organized_by} on {self.event_datetime.strftime('%Y-%m-%d %H:%M')}"
    
# Participation model
class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} registered for {self.event.title} on {self.registered_at.strftime('%Y-%m-%d %H:%M')}"
