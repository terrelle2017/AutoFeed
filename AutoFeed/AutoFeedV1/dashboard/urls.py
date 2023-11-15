from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("light/on/", views.lightsOn, name="index"),
    path("light/off/", views.lightsOff, name="index"),
]