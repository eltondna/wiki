from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.newpage, name="newpage"),
    path("search", views.search, name="search"),
    path("random", views.random, name="random"),
    path("<str:page>", views.pages, name ="page"),
    
]
