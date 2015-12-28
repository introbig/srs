from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Deck
from django import forms
from .models import Card

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class DeckForm(forms.ModelForm):
    class Meta:
    	model = Deck
    	fields = ["user", "name"]


class CardForm(forms.ModelForm):
	class Meta:
		model = Card
		fields = ["question", "answer", "deck"]