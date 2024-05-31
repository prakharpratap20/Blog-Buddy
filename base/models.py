from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class Topic(models.Model):
    """Model for topics"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    """Model for the room"""
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name="participants", blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Class to order the rooms"""
        ordering = ["-updated", "-created"]

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    """Model for the messages"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Class to order the messages"""
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.body[0:50]
