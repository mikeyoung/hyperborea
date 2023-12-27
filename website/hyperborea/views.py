from django.http import JsonResponse
from django.shortcuts import render
from .models import Spell
import json

def spells(request):
    filter_by = request.GET.get("filter_by")
    render_as = request.GET.get("render_as")

    spells = None

    if filter_by != None:
        match filter_by:
            case "lists":
                spells = Spell.objects.filter(description__icontains='<uL>')
        match filter_by:
            case "dash":
                spells = Spell.objects.filter(description__icontains='-')
    else:
        spells = Spell.objects.all()

    if render_as == "json":
        #todo write json code that works
        #pass
        return JsonResponse(list(spells.values()), status=201, safe=False)
    else:
        return render(request, "hyperborea/spells.html", {
            'spells': spells
        })