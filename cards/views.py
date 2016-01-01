from django.shortcuts import render
from .models import Card
from .models import Deck
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .forms import DeckForm
from .forms import CardForm
import pandas as pd
import numpy
import csv


def redirect_view(request):
    if request.user.is_authenticated():
        query_set = Deck.objects.filter(user=request.user.id)
        return render(request, "cards/decks_template.html", {"query_set": query_set})
    return render(request, "cards/home_template.html")


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
            query_set = Deck.objects.filter(user__exact=request.user.id)
            return render(request, "cards/decks_template.html", {"query_set": query_set})
        form = CreateUserForm(request.POST)
        return render(request, "cards/register_template.html", {"form": form})
    form = CreateUserForm()
    return render(request, "cards/register_template.html", {"form": form})


# def card_view(request, id):
#     id = 1
#     query_set = Card.objects.get(pk=1)
#     return render(request, "cards/card_template.html", {"query_set":query_set})


@csrf_exempt
def decks_view(request):
    if request.method == "POST" and request.POST.get("function") == "deleteDeck":
        Deck.objects.get(pk=request.POST.get("id")).delete()
        query_set = Deck.objects.filter(user__exact=request.user.id)
        return render(request, "cards/decks_template.html", {"query_set": query_set})
    elif request.method == "POST" and request.FILES.get("bulkupload"):
        try:
            df = pd.read_csv(request.FILES.get("bulkupload"))
            df.columns = [x.lower() for x in df.columns]
            for item in set(df["deck"]):
                if item not in set(item.name for item in Deck.objects.filter(user=request.user.id)):
                    Deck.objects.create(name=item, user=request.user)
            for index, values  in df[["question", "answer", "deck"]].iterrows():
                Card.objects.create(question=values[0], answer=values[1], deck=next(x for x in Deck.objects.filter(user=request.user) if x.name==values[2]))
        except:
            return HttpResponse("Error in CSV. Please check columns and file format are correct.") 
    elif request.GET.get("csv_down"):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="all_cards.csv"'
        writer = csv.writer(response)
        writer.writerow(['question', 'answer', 'deck'])
        for item in Card.objects.filter(deck__user=request.user):
            writer.writerow([item.question, item.answer, item.deck.name])
        return response
    elif request.method == "POST":
        form = DeckForm({"user": request.user.id, "name": request.POST.get("deckname")})
        if form.is_valid():
            form.save()
    query_set = Deck.objects.filter(user__exact=request.user.id)
    return render(request, "cards/decks_template.html", {"query_set": query_set})


@csrf_exempt
def edit_cards_view(request, id):
    if request.method == "POST" and request.POST.get("function") == "deleteCard":
        card_instance = Card.objects.get(pk=request.POST.get("card_id"))
        card_instance.delete()
    elif request.method == "POST" and request.POST.get("function") == "updateCard":
        card_instance = Card.objects.get(pk=request.POST.get("id"))
        card_instance.question = request.POST.get("question")
        card_instance.answer = request.POST.get("answer")
        card_instance.save()
    elif request.method == "POST":
        form = CardForm({"question":request.POST.get("question"), "answer": request.POST.get("answer"), "deck": id})
        if form.is_valid():
            form.save()
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
    if not (Card.objects.filter(deck__exact=id).exists()):
        query_set = Card.objects.filter(deck__exact=id)
        deck_name = Deck.objects.get(pk=id).name
        deck_id = Deck.objects.get(pk=id).id
        return render(request, "cards/edit_cards_template.html", {"query_set": query_set, "deck_name": deck_name, "deck_id":deck_id})
    card = sorted(Card.objects.filter(deck__exact=id), key=lambda x: x.current_rank)[0]
    return render(request, "cards/card_review_template.html", {"card":card})



#  it is currently moving from lowest to highest rank
def rank_update_view(request, deck_id, card_id, rank):
    card_instance = Card.objects.get(id__exact=card_id)
    card_instance.current_rank = rank
    card_instance.save()
    card = sorted(Card.objects.filter(deck__exact=deck_id), key=lambda x: x.current_rank)[0]
    return render(request, "cards/card_review_template.html", {"card":card})


