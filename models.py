# This is the Django frame for the GUI
from django.db import models
from django.contrib.auth.models import User

class Beacon(models.Model):
    name = models.CharField(max_length=100)
    target_ip = models.GenericIPAddressField()
    connected = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Command(models.Model):
    beacon = models.ForeignKey(Beacon, on_delete=models.CASCADE)
    command = models.CharField(max_length=255)

class Log(models.Model):
    beacon = models.ForeignKey(Beacon, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    log_data = models.TextField()

class Note(models.Model):
    SEVERITY_CHOICES = (
        ('normal', 'Normal'),
        ('critical', 'Critical'),
    )

    beacon = models.ForeignKey(Beacon, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    host_ip = models.GenericIPAddressField()
    target_ip = models.GenericIPAddressField()
    severity = models.CharField(max_length=8, choices=SEVERITY_CHOICES, default='normal')

class Event(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='events')
    sequence_number = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

class Meta:
    unique_together = ('note', 'sequence_number')

class Note(models.Model):
    SEVERITY_CHOICES = (
        ('normal', 'Normal'),
        ('critical', 'Critical'),
    )

    beacon = models.ForeignKey(Beacon, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    host_ip = models.GenericIPAddressField()
    target_ip = models.GenericIPAddressField()
    severity = models.CharField(max_length=8, choices=SEVERITY_CHOICES, default='normal')

