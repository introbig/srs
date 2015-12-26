from django.conf.urls import url, include
from . import views


urlpatterns = [
  url('^card_template/(?P<id>\d+)/$', views.card_view, name="card"),
  url('^decks_template', views.decks_view, name="decks"),
  url('^edit_cards_template/(?P<id>\d+)/$', views.edit_cards_view, name="edit_cards"),
  url('^delete_card_template/(?P<id1>\d+)/(?P<id2>\d+)/$', views.delete_card_view, name="delete_card")
]