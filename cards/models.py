from django.db import models
from django.contrib.auth.models import User

class Deck(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(User)
    def __str__(self):
        return str(self.name)

class Card(models.Model):
    question = models.TextField(default="", null=True, blank=True)
    answer = models.TextField(default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    current_rank = models.IntegerField(null=True, blank=True, default=0)
    last_seen = models.DateTimeField(null=True, blank=True)
    deck = models.ForeignKey(Deck)
    image = models.CharField(max_length=200, null=True, blank=True)
    recording = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return str(self.question)

