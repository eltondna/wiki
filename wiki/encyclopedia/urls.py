from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:page>", views.pages, name ="page"),
]
