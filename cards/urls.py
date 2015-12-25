from django.conf.urls import url, include
from . import views


urlpatterns = [
  url(r'^home/', views.hello_world, name="hello_world"),
  url('^card/(?P<id>\d+)/$', views.card_view, name="card"),

]