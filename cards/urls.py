from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
  url(r'^home/', views.hello_world, name="hello_world"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
