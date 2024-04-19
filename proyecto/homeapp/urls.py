from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from homeapp import views

urlpatterns = [
    path('', views.home, name="Home"),
]