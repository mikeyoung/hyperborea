from django.urls import path

from . import views

urlpatterns = [
    path('', views.spells, name='index'),
    path('create-json', views.create_json, name='create-json'),
    path('get-spell-description', views.get_spell_description, name='get-spell-description'),
]