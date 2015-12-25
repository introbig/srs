from django.conf.urls import url, include
from . import views


urlpatterns = [
  url('^card_template/(?P<id>\d+)/$', views.card_view, name="card"),
  url('^decks_template', views.decks_view, name="decks"),

]