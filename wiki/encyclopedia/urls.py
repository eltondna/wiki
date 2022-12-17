from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("<str:page>", views.pages, name ="page"),
   path("newpage", views.newPage, name="newPage")
]
