from django.shortcuts import render
from .models import Card
from .models import Deck
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def home_view(request):
	return render(request, "cards/home_template.html")

def about_view(request):
	return render(request, "cards/about_template.html")

def register_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return render(request, "cards/decks_template.html")
        form = CreateUserForm(request.POST)
        return render(request, "cards/register_template.html", {"form": form})
    form = CreateUserForm()
    return render(request, "cards/register_template.html", {"form": form})


def card_view(request, id):
    id = 1
    query_set = Card.objects.get(pk=1)
    return render(request, "cards/card_template.html", {"query_set":query_set})


def decks_view(request):
    query_set = Deck.objects.filter(user__exact=request.user.id)
    return render(request, "cards/decks_template.html", {"query_set": query_set})


def edit_cards_view(request, id):
    query_set = Card.objects.filter(deck__exact=id)
    deck_name = Deck.objects.get(pk=id).name
    deck_id = Deck.objects.get(pk=id).id
    return render(request, "cards/edit_cards_template.html", {"query_set": query_set, "deck_name": deck_name, "deck_id":deck_id})


#  add user validation
def delete_card_view(request, id1, id2):
    model_instance = Card.objects.get(pk = id1)
    model_instance.delete()
    query_set = Card.objects.filter(deck__exact=id2)
    deck_name = Deck.objects.get(pk=id2).name
    deck_id = Deck.objects.get(pk=id2).id
    return render(request, "cards/edit_cards_template.html", {"query_set": query_set, "deck_name": deck_name, "deck_id":deck_id})


def card_review_view(request, id):
	#card = Card.objects.filter(id__exact=request.id)[]
	card = sorted(Card.objects.filter(deck__exact=id), key=lambda x: x.current_rank)[0]
	return render(request, "cards/card_review_template.html", {"card":card})


#  it is currently moving from lowest to highest rank
def rank_update_view(request, deck_id, card_id, rank):
    card_instance = Card.objects.get(id__exact=card_id)
    card_instance.current_rank = rank
    card_instance.save()
    card = sorted(Card.objects.filter(deck__exact=deck_id), key=lambda x: x.current_rank)[0]
    return render(request, "cards/card_review_template.html", {"card":card})