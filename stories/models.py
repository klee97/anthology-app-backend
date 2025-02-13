from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid


class Story(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    link = models.TextField(blank=True)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,  # Automatically generate a new UUID
        editable=False       # Prevent manual editing of the UUID
    )
    
    def __str__(self):        
        return self.title

class StoryEval(models.Model):
    
    class Status(models.TextChoices):
        UNREAD = 'UR', _('Unread')
        IN_PROGRESS = 'IP', _('In Progress')
        READ = 'R', _('Read')

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,  # Automatically generate a new UUID
        editable=False       # Prevent manual editing of the UUID
    )
    dateFinished = models.DateField()
    dateStarted = models.DateField()
    rating = models.IntegerField(default=0)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="evaluations")
    reader = models.ForeignKey("Reader", on_delete=models.CASCADE, related_name="evaluations")
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.UNREAD,
    )
    class Meta:
        unique_together = ("story", "reader")  # Prevents duplicate evaluations from the same reader
        
    def __str__(self):
        return f"{self.reader.user.username} -> {self.story.title} ({self.rating})"
class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="reader")
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,  # Automatically generate a new UUID
        editable=False       # Prevent manual editing of the UUID
    )
    
    def __str__(self):
        return f"Reader: {self.user.username}"


    
