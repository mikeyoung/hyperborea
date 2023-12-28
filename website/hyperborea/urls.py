from django.urls import path

from . import views

urlpatterns = [
    path("", views.spells, name="index"),
    path("create-json", views.create_json, name="create-json"),
    path("get-spells", views.get_spells, name="get-spells"),
]