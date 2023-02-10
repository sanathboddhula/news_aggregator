from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("home", views.index),
    path("health", views.health),
    path("business", views.business),
    path("sports", views.sports),
    path("entertainment", views.entertainment),
    path("science", views.science),
    path("technology", views.technology),
]