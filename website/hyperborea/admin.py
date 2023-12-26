from django.contrib import admin
from hyperborea.models import Spell, CharacterClass, SpellListItem

# Register your models here.
admin.site.register(Spell)
admin.site.register(CharacterClass)
admin.site.register(SpellListItem)