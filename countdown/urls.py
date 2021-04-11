# countdown/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.countdown_index, name="countdown_index"),
]
