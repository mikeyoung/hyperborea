from django.shortcuts import render
from .models import Spell

def spells(request):
    filter_by = request.GET.get("filter_by")

    spells = None

    if filter_by != None:
        match filter_by:
            case "lists":
                spells = Spell.objects.filter(description__icontains='<uL>')
    else:
        spells = Spell.objects.all()

    return render(request, "hyperborea/spells.html", {
        'spells': spells
    })