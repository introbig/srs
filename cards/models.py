from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(User)

class Card(models.Model):
    question = models.TextField(default="", null=True, blank=True)
    answer = models.TextField(default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    current_rank = models.CharField(max_length=200, null=True, blank=True)
    last_seen = models.DateTimeField(null=True, blank=True)
    deck = models.ForeignKey(Deck)
    image = models.CharField(max_length=200, null=True, blank=True)
    recording = models.CharField(max_length=200, null=True, blank=True)    

