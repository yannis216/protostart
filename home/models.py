from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    cooperation_partners = models.TextField(blank=True)
    logo = models.CharField(max_length=100, default="protostart_logo_website-min.png")

    def __str__(self):
        return self.title
