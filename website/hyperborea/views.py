from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from .models import CharacterClass, Spell, SpellListItem
import json
from django.contrib.auth.decorators import login_required
import os
from website.settings import BASE_DIR
from django.db.models import Q

def spells(request):
    character_class = None
    spell_level = None

    value_rules = {}

    if request.method == "POST":
        if request.POST.get('class') != 'all':
            character_class = CharacterClass.objects.get(pk=int(request.POST.get('class')))
            value_rules['character_class'] = character_class
        if request.POST.get('level') != 'all':
            spell_level = request.POST.get('level')
            value_rules['level'] = spell_level
    else:
        character_class = 'all'
        spell_level = 'all'

    spell_list = None

    class_list = CharacterClass.objects.all()

    spell_list = SpellListItem.objects.filter(**value_rules)

    # q_objects = Q()

    # if character_class != 'all':
    #     q_objects.add(Q(character_class=character_class), Q.AND)
    
    # if spell_level != 'all':
    #     q_objects.add(Q(level=spell_level), Q.AND)
    
    # spell_list = SpellListItem.objects.filter(q_objects)


    
    return render(request, "hyperborea/spells.html", {
        'spell_list': spell_list,
        'class_list': class_list,
        'levels': ['1','2','3'],
        'selected_character_class': character_class,
        'selected_level': spell_level
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