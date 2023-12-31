from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from .models import CharacterClass, Spell, SpellListItem
import json
from django.contrib.auth.decorators import login_required
import os
from website.settings import BASE_DIR
from django.core import serializers

def spells(request):
    character_class = 'all'
    spell_level = 'all'
    value_rules = {}

    class_list = CharacterClass.objects.all()

    return render(request, 'hyperborea/spells.html', {
        'class_list': class_list,
        'levels': ['1','2','3'],
    })

def get_spells(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    
    character_class = 'all'
    spell_level = 'all'
    value_rules = {}

    submitted_data = json.loads(request.body)

    submitted_spellbook = submitted_data.get('spellbook_json_string')
    submitted_class = submitted_data.get('character_class')
    submitted_level = submitted_data.get('level')
    submitted_scope = submitted_data.get('scope')

    if submitted_class != 'all' and submitted_class != None:
        character_class = CharacterClass.objects.get(pk=int(submitted_class))
        value_rules['character_class'] = character_class

    if submitted_level != 'all' and submitted_level != None:
        spell_level = submitted_level
        value_rules['level'] = spell_level

    if submitted_scope == 'spellbook' and submitted_spellbook != None:
        if submitted_spellbook == '':
            submitted_spellbook = []
        else:
            submitted_spellbook = json.loads(submitted_spellbook)

        value_rules['spell__in'] = submitted_spellbook

    spell_list = SpellListItem.objects.filter(**value_rules).order_by('spell')

    if character_class == 'all' and spell_level == 'all':
        spell_list = spell_list.distinct()
    
    page_title = "All Spells of The Realm"

    if character_class == 'all' and spell_level != 'all':
        page_title = f'All Level {spell_level} Spells'
    elif character_class != 'all' and spell_level == 'all':
        page_title = f'All { str(character_class).capitalize() } Spells'
    elif character_class != 'all' and spell_level != 'all':
        page_title = f'All Level { spell_level } { str(character_class).capitalize() } Spells'
    
    if submitted_scope == 'spellbook':
        page_title = f'{page_title} in Spellbook'

    returned_spells = []

    for spell in spell_list:
        returned_spells.append({
            'name': spell.spell_name,
            'level': spell.level,
            'character_class': spell.class_name,
            'spell_id': spell.spell_id
        })

    return JsonResponse({
        'spell_list': returned_spells,
        'page_title': page_title,
    })
    


def get_spell_description(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    
    data = json.loads(request.body)
    
    spell_id = data.get('spell_id')

    if spell_id == None:
        return HttpResponseBadRequest()
    
    spell = Spell.objects.get(pk=spell_id)
    spell_name = spell.name
    spell_description = spell.description
        
    return JsonResponse({
        'success': True,
        'spell_name': spell_name,
        'spell_description': spell_description
    }, status=201)


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

        return JsonResponse({'success': True}, status=201)
    
    except:
        return JsonResponse({'success': False}, status=500)