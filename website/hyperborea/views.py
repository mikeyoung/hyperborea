from django.http import JsonResponse
from django.shortcuts import render
from .models import CharacterClass, Spell, SpellListItem
import json
from django.contrib.auth.decorators import login_required
import os
from website.settings import BASE_DIR

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
        return JsonResponse(list(spells.values()), status=201, safe=False)
    else:
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

        classes = CharacterClass.objects.all()
        file_path = os.path.join(BASE_DIR, 'hyperborea/static/hyperborea/json/character_classes.json')

        with open(file_path, 'w') as file:
            json.dump(list(classes.values()), file)

        spell_list_items = SpellListItem.objects.all()
        file_path = os.path.join(BASE_DIR, 'hyperborea/static/hyperborea/json/spell_list_itemss.json')

        with open(file_path, 'w') as file:
            json.dump(list(spell_list_items.values()), file)

        return JsonResponse({"success": True}, status=201)
    
    except:
        return JsonResponse({"success": False}, status=500)