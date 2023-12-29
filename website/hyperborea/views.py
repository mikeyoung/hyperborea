from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from .models import CharacterClass, Spell, SpellListItem
import json
from django.contrib.auth.decorators import login_required
import os
from website.settings import BASE_DIR
from django.db.models import Q

def spells(request):
    filter_by = request.GET.get("filter_by")
    render_as = request.GET.get("render_as")

    spells = None
    class_list = CharacterClass.objects.all()

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
            'spells': spells,
            'class_list': class_list,
            'levels': range(1,7)
        })
    
def get_spells(request):
    if request.method != "POST":
        return HttpResponseBadRequest()

    char_class = request.POST.get("class")
    spell_level = request.POST.get("level")

    q_objects = Q()

    if char_class != 'all':
        q_objects.add(Q(character_class=char_class), Q.AND)
    
    if spell_level != 'all':
        q_objects.add(Q(level=spell_level), Q.AND)
    
    spells = SpellListItem.objects.filter(q_objects)
    
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