from django.shortcuts import render
from .models import Card
from .models import Deck
from django.contrib.auth.models import User



def card_view(request, id):
    id = 1
    query_set = Card.objects.get(pk=1)
    return render(request, "cards/card_template.html", {"query_set":query_set})


def decks_view(request):
    query_set = Deck.objects.all()
    return render(request, "cards/decks_template.html", {"query_set": query_set})
