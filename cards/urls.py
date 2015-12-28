from django.conf.urls import url, include
from . import views


urlpatterns = [
  url('^card_template/(?P<id>\d+)/$', views.card_view, name="card"),
  url('^decks_template', views.decks_view, name="decks"),
  url('^edit_cards_template/(?P<id>\d+)?/?$', views.edit_cards_view, name="edit_cards"),
  url('^delete_card_template/(?P<id1>\d+)/(?P<id2>\d+)/$', views.delete_card_view, name="delete_card"),
  url('^rank_update_template/(?P<id>\d+)/(?P<rank>\d+)/$', views.rank_update_view, name="rank_update"),
  url('^card_review_template/(?P<id>\d+)/$', views.card_review_view, name="card_review"),
  url('^rank_update_template/(?P<deck_id>\d+)/(?P<card_id>\d+)/(?P<rank>\d+)/$', views.rank_update_view, name="rank_update"),
  url('^about_template', views.about_view, name="about"),
  url('^register_template', views.register_view, name="register"),
  url('^home_template', views.home_view, name="home"),


  url(r'^$', views.redirect_view),

]