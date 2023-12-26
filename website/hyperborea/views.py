from django.shortcuts import render
from .models import Spell

def spells(request):
    spells = Spell.objects.all()

    return render(request, "hyperborea/spells.html", {
        'spells': spells
    })