from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from .models import Spell
import json
from django.contrib.auth.decorators import login_required
import os
from website.settings import BASE_DIR
from django.db.models import Q

def spells(request):
    filter_by = request.GET.get("filter_by")
    render_as = request.GET.get("render_as")

    spells = None

    if filter_by != None:
        match filter_by:
            case "lists":
                spells = Spell.objects.filter(description__icontains='<uL>')
            case "dash":
                spells = Spell.objects.filter(description__icontains='-')
            case "missing_class":
                spells = Spell.objects.filter(magician_level=0, cryomancer_level=0, illusionist_level=0, necromancer_level=0, pyromancer_level=0, witch_level=0, cleric_level=0, druid_level=0)
    else:
        spells = Spell.objects.all()

    if render_as == "json":
        return JsonResponse(list(spells.values()), status=201, safe=False)
    else:
        return render(request, "hyperborea/spells.html", {
            'spells': spells
        })
    
def get_spells(request):
    if request.method != "POST":
        return HttpResponseBadRequest()
    
    q_objects = Q()

    character_class = request.POST.get("class")
    spell_level = request.POST.get("level")
    
    spells = Spell.objects.all()
    
    return render(request, "hyperborea/spells.html", {
        'spells': spells
    })


@login_required
def create_json(request):
    try: 
        spells = Spell.objects.all()
        file_path = os.path.join(BASE_DIR, 'hyperborea/static/hyperborea/json/spells.json')

        with open(file_path, 'w') as file:
            json.dump(list(spells.values()), file)

        return JsonResponse({"success": True}, status=201)
    
    except:
        return JsonResponse({"success": False}, status=500)