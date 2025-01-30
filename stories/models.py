from django.db import models
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