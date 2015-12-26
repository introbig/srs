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


def edit_cards_view(request, id):
    query_set = Card.objects.filter(deck__exact=id)
    deck_name = Deck.objects.get(pk=id).name
    deck_id = Deck.objects.get(pk=id).id
    return render(request, "cards/edit_cards_template.html", {"query_set": query_set, "deck_name": deck_name, "deck_id":deck_id})


def delete_card_view(request, id1, id2):
    model_instance = Card.objects.get(pk = id1)
    model_instance.delete()

    query_set = Card.objects.filter(deck__exact=id2)
    deck_name = Deck.objects.get(pk=id2).name
    deck_id = Deck.objects.get(pk=id2).id
    return render(request, "cards/edit_cards_template.html", {"query_set": query_set, "deck_name": deck_name, "deck_id":deck_id})
